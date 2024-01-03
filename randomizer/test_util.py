from django.test import TestCase

from randomizer.models import Category, Word
from randomizer.util import random_word, pluralize


class TestUtilsModule(TestCase):
    def setUp(self):
        # Set up method to add some data for testing
        self.category = Category.objects.create(name="Test")
        self.words =\
            [Word.objects.create(
                name=f"word{i}"
            ) for i in range(10)]
        for word in self.words:
            word.categories.add(self.category, through_defaults={})
            word.save()

    def test_random_word(self):
        # Test the random_word function
        random_word_result = random_word("Test")
        self.assertIn(random_word_result, self.words)

    def test_pluralize(self):
        # Test the pluralize function
        self.assertEqual('boxes', pluralize('box'))
        self.assertEqual('churches', pluralize('church'))
        self.assertEqual('boys', pluralize('boy'))
