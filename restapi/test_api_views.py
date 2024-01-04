import unittest
from unittest import mock

from django.test import TestCase
from randomizer.models import Word, Category
from randomizer.picker import generate_band_name

import randomizer.models as models
from restapi.views import (
    WordListCreateAPIView,
    WordUpdateDeleteAPIView,
    CategoryListCreateAPIView,
    CategoryUpdateDeleteAPIView,
)


class ViewTestCase(unittest.TestCase):
    @mock.patch.object(models.Word, 'objects')
    def test_get_words(self, mock_objects):
        mock_objects.all.return_value = ['word1', 'word2', 'word3']

        words = WordListCreateAPIView.get_words()

        self.assertEqual(words, ['word1', 'word2', 'word3'])
        mock_objects.all.assert_called_once()

    @mock.patch.object(models.Word, 'objects')
    def test_get_words_for_update_delete_view(self, mock_objects):
        mock_objects.all.return_value = ['word1', 'word2', 'word3']

        words = WordUpdateDeleteAPIView.get_words()

        self.assertEqual(words, ['word1', 'word2', 'word3'])
        mock_objects.all.assert_called_once()

    @mock.patch.object(models.Category, 'objects')
    def test_get_categories(self, mock_objects):
        mock_objects.all.return_value = ['category1', 'category2', 'category3']

        categories = CategoryListCreateAPIView.get_categories()

        self.assertEqual(categories, ['category1', 'category2', 'category3'])
        mock_objects.all.assert_called_once()

    @mock.patch.object(models.Category, 'objects')
    def test_get_categories_for_update_delete_view(self, mock_objects):
        mock_objects.all.return_value = ['category1', 'category2', 'category3']

        categories = CategoryUpdateDeleteAPIView.get_categories()

        self.assertEqual(categories, ['category1', 'category2', 'category3'])
        mock_objects.all.assert_called_once()


class PickerTestCase(TestCase):
    def setUp(self):
        Word.objects.create(name='testword1')
        Word.objects.create(name='testword2')
        Category.objects.create(name='testcategory1')
        Category.objects.create(name='testcategory2')

    def test_generate_band_name(self):
        band_name = generate_band_name()
        self.assertIsNotNone(band_name)


if __name__ == "__main__":
    unittest.main()
