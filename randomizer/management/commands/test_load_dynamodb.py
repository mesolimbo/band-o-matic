import unittest
from unittest.mock import patch, MagicMock

from django.core.management import call_command
from django.test import TestCase

from randomizer.management.commands import load_dynamodb


class TestLoadDynamoDB(TestCase):
    @patch('boto3.resource')
    def setUp(self, mock_resource):
        self.command = load_dynamodb.Command()
        self.mock_dynamodb = mock_resource.return_value
        self.mock_table = MagicMock()
        self.mock_dynamodb.Table.return_value = self.mock_table

    def test_init_tables(self):
        self.command.reset_tables(self.mock_dynamodb)
        self.mock_table.delete.assert_called()
        self.mock_table.wait_until_not_exists.assert_called()
        self.mock_dynamodb.create_table.assert_called()

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='category,name\nAdjective,Adamant')
    def test_read_csv_file(self, _):
        rows = self.command.read_csv_file('mock.csv')
        self.assertEqual(rows, [['Adjective', 'Adamant']])

    def test_process_rows(self):
        rows = [('Adjective', 'Adamant'), ('Adjective', 'Adroit')]
        categories, word_category_pairs = self.command.process_rows(rows)
        self.assertEqual(categories, {'Adjective'})
        self.assertEqual(word_category_pairs, {'Adamant': {'Adjective'}, 'Adroit': {'Adjective'}})

    def test_insert_categories(self):
        categories = {'Adjective'}
        self.command.insert_categories(self.mock_table, categories)
        self.mock_table.batch_writer().__enter__().put_item.assert_called_with(Item={'name': 'Adjective'})

    def test_insert_words(self):
        word_category_pairs = {'Adamant': {'Adjective'}}
        self.command.insert_words(self.mock_table, word_category_pairs)
        self.mock_table.batch_writer().__enter__().put_item.assert_called_with(
            Item={'name': 'Adamant', 'category_ids': ['Adjective']})

    @patch('randomizer.management.commands.load_dynamodb.Command.insert_words')
    @patch('randomizer.management.commands.load_dynamodb.Command.insert_categories')
    @patch('randomizer.management.commands.load_dynamodb.Command.process_rows')
    @patch('randomizer.management.commands.load_dynamodb.Command.load_csv_data')
    @patch('randomizer.management.commands.load_dynamodb.Command.init_db')
    def test_handle(self, mock_init_db, mock_load_csv_data, mock_process_rows, mock_insert_categories,
                    mock_insert_words):
        mock_init_db.return_value = (self.mock_table, self.mock_table)
        mock_load_csv_data.return_value = [('Adjective', 'Adamant'), ('Adjective', 'Adroit')]
        mock_process_rows.return_value = ({'Adjective'}, {'Adamant': {'Adjective'}, 'Adroit': {'Adjective'}})

        call_command('load_dynamodb')

        mock_init_db.assert_called_once()
        mock_load_csv_data.assert_called_once()
        mock_process_rows.assert_called_once_with(mock_load_csv_data.return_value)
        mock_insert_categories.assert_called_once_with(self.mock_table, mock_process_rows.return_value[0])
        mock_insert_words.assert_called_once_with(self.mock_table, mock_process_rows.return_value[1])

    @patch('randomizer.management.commands.load_dynamodb.Command.reset_tables')
    @patch('boto3.resource')
    def test_init_db(self, mock_resource, mock_reset_tables):
        mock_resource.return_value = self.mock_dynamodb
        mock_reset_tables.return_value = (self.mock_table, self.mock_table)

        result = self.command.init_db()

        mock_resource.assert_called_once()
        mock_reset_tables.assert_called_once_with(self.mock_dynamodb)
        self.assertEqual(result, (self.mock_table, self.mock_table))

    @patch('randomizer.management.commands.load_dynamodb.Command.read_csv_file')
    def test_load_csv_data(self, mock_read_csv_file):
        mock_read_csv_file.return_value = [('Adjective', 'Adamant'), ('Adjective', 'Adroit')]
        options = {'csv_path': 'mock.csv'}

        result = self.command.load_csv_data(options)

        mock_read_csv_file.assert_called_once_with('mock.csv')
        self.assertEqual(result, [('Adjective', 'Adamant'), ('Adjective', 'Adroit')])
