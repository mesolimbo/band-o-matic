import boto3
import csv
import logging

from concurrent.futures import ThreadPoolExecutor

from django.core.management.base import BaseCommand

BANDOMATIC_CATEGORIES = 'bandomatic_Categories'
BANDOMATIC_WORDS = 'bandomatic_Words'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import CSV data into DynamoDB: ./manage.py load_dynamodb <optional_csv_path>'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='?', default='./defaut_words.csv')

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        dynamodb = boto3.resource('dynamodb')

        logger.info('Initializing tables...')
        categories_table, words_table = self.init_tables(dynamodb)

        logger.info(f'Loading data from {csv_path} into DynamoDB...')
        try:
            rows = self.read_csv_file(csv_path)
        except FileNotFoundError:
            logger.info(f'File not found {csv_path}')
            return

        categories, word_category_pairs = self.process_rows(rows)

        self.insert_categories(categories_table, categories)
        self.insert_words(words_table, word_category_pairs)

    def init_tables(self, dynamodb):
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(self.clear_and_recreate_table, dynamodb, name)
                for name in (BANDOMATIC_CATEGORIES, BANDOMATIC_WORDS)
            ]
            return [future.result() for future in futures]

    def clear_and_recreate_table(self, dynamodb, table_name):
        self.clear_table(dynamodb, table_name)
        return self.create_new_table(table_name, dynamodb)

    @staticmethod
    def clear_table(dynamodb, table_name):
        table = dynamodb.Table(table_name)
        try:
            logger.info(f'Deleting table {table_name}')
            table.delete()
            table.wait_until_not_exists()
            logger.info(f'Table deleted {table_name}')
        except dynamodb.meta.client.exceptions.ResourceNotFoundException:
            pass

    @staticmethod
    def create_new_table(name, dynamodb):
        logger.info(f'Creating table {name}')
        new_table = dynamodb.create_table(
            TableName=name,
            KeySchema=[{'AttributeName': 'name', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'name', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        new_table.wait_until_exists()
        logger.info(f'Table created {name}')

        return new_table

    @staticmethod
    def read_csv_file(csv_path):
        logger.info(f'Reading rows from {csv_path}...')
        try:
            with open(csv_path, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)[1:]  # Skip the header row
        except FileNotFoundError:
            raise

        return rows

    @staticmethod
    def process_rows(rows):
        logger.info('Processing rows...')
        categories = set()
        word_category_pairs = {}

        for row in rows:
            category_name, word_name = row
            categories.add(category_name)
            word_category_pairs.setdefault(word_name, set()).add(category_name)
            logger.info(f'Processed row ({category_name}, {word_name})')

        return categories, word_category_pairs

    @staticmethod
    def insert_categories(categories_table, categories):
        with categories_table.batch_writer() as batch:
            for category_name in categories:
                logger.info(f'Inserting category {category_name}')
                batch.put_item(Item={'name': category_name})

    @staticmethod
    def insert_words(words_table, word_category_pairs):
        with words_table.batch_writer() as batch:
            for word_name, category_names in word_category_pairs.items():
                logger.info(f'Inserting word {word_name} with categories {category_names}')
                batch.put_item(Item={'name': word_name, 'category_ids': list(category_names)})
