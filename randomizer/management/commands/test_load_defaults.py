from django.core.management import call_command
from django.test import TestCase

import csv
import os


from randomizer.management.commands import load_defaults
from randomizer.models import Word, Category, WordCategory


class TestLoadDefaults(TestCase):
    def setUp(self):
        self.command = load_defaults.Command()
        self.csv_file = "./test_words.csv"
        rows = [
            {"name": "Fast", "category": "Adjective"},
            {"name": "Quickly", "category": "Adverb"},
            {"name": "Car", "category": "Noun"}
        ]

        with open(self.csv_file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category"])
            writer.writeheader()
            writer.writerows(rows)

    def test_load_defaults(self):
        call_command('load_defaults', self.csv_file)

        self.assertEqual(Category.objects.count(), 3)
        self.assertEqual(Word.objects.count(), 3)
        self.assertEqual(WordCategory.objects.count(), 3)

        vals_sorted = Category.objects.values_list('name', flat=True).order_by('name')
        self.assertQuerysetEqual(vals_sorted, ["Adjective", "Adverb", "Noun"])

        words_sorted = Word.objects.values_list('name', flat=True).order_by('name')
        self.assertQuerysetEqual(
            words_sorted,
            ['Car', 'Fast', 'Quickly']
        )

    def test_reloading_defaults_raises_error(self):
        call_command('load_defaults')

    def tearDown(self):
        os.remove(self.csv_file)
