import random

from randomizer.models import Word, Category, WordCategory


def random_word(category_name):
    # Get the specified category by name
    category = Category.objects.filter(name=category_name).first()

    # Get all words associated with this category
    words = Word.objects.filter(wordcategory__category=category)

    # Pick a random word
    return random.choice(words)


def generate_band_name():
    # Logic to generate a band name
    return f'The {random_word('Adverb')} {random_word('Adjective')} {random_word('Noun')}s!'
