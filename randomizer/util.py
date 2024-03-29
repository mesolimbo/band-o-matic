import random

from awslambda.helpers import grammar
from randomizer.models import Category, Word


def random_word(category_name):
    # Get the specified category by name
    category = Category.objects.filter(name=category_name).first()

    # Get all words associated with this category
    words = Word.objects.filter(wordcategory__category=category)

    # Pick a random word
    return random.choice(words)


def pluralize(word):
    return grammar.plural(word)
