import random
import re

import inflect

from randomizer.models import Category, Word


def random_word(category_name):
    # Get the specified category by name
    category = Category.objects.filter(name=category_name).first()

    # Get all words associated with this category
    words = Word.objects.filter(wordcategory__category=category)

    # Pick a random word
    return random.choice(words)


def pluralize(word):
    p = inflect.engine()
    plural = p.plural_noun(str(word))
    # Fix buggy y plurals
    clean_plural = re.sub('(?<![aeiou])ys$', 'ies', plural)

    return clean_plural
