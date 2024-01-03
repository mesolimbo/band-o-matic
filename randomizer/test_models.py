from django.test import TestCase

from randomizer.models import Category, Word, WordCategory  # update this import statement as per your module structure


class TestCategoryModel(TestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(name="Cat1")
        self.cat2 = Category.objects.create(name="Cat2")

    def test_category_str(self):
        self.assertEqual(str(self.cat1), "Cat1")


class TestWordModel(TestCase):
    def setUp(self):
        self.word1 = Word.objects.create(name="Word1")

    def test_word_str(self):
        self.assertEqual(str(self.word1), "Word1")


class TestWordCategoryModel(TestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(name="Cat1")
        self.word1 = Word.objects.create(name="Word1")
        self.wordCat1 = (
            WordCategory.objects.create(word=self.word1, category=self.cat1))

    def test_word_category_creation(self):
        self.assertTrue(isinstance(self.wordCat1, WordCategory))
        self.assertEqual(
            self.word1.name + " " + self.cat1.name,
            self.wordCat1.__str__()
        )
