from csv import DictReader
from django.core.management import BaseCommand

from randomizer.models import Word, Category, WordCategory

CATEGORIES = ['Adjective', 'Adverb', 'Noun', 'Famous', 'Verb']

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the Word defaults from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    """To load default words, run command from the project root: `./manage.py load_defaults`"""
    help = "Loads default words from defaut_words.csv into our Word model"

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='?', default='./defaut_words.csv')

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        if Category.objects.exists() or Word.objects.exists():
            print('Default data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading default Word and Category defaults")
        with open(csv_path) as file:  # using a context manager for file handling
            for row in DictReader(file):
                category, _ = Category.objects.get_or_create(name=row['category'])
                word, _ = Word.objects.get_or_create(name=row['name'])
                word_category, _ = WordCategory.objects.get_or_create(word=word, category=category)
