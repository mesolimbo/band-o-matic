from django.test import TestCase, Client
from django.urls import reverse

from randomizer.models import Category, Word
from greet import views


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.privacy_url = reverse('privacy')

        # Initialize test database
        categories = ['Adjective', 'Adverb', 'Famous', 'Noun', 'Verb']
        for category_name in categories:
            category = Category.objects.create(name=category_name)
            word = Word.objects.create(name=f'test_{category_name}')
            word.wordcategory_set.create(category=category)

    def test_generate_band_data(self):
        data = views.generate_band_data()

        self.assertTrue('band_name' in data)
        self.assertEqual(data['title'], 'Welcome!')
