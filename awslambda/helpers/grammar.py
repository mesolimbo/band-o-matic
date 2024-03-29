import re

import inflect


def plural(word):
    p = inflect.engine()
    raw_plural = p.plural_noun(str(word))
    # Fix buggy "y" plurals
    clean_plural = re.sub('(?<![aeiou])ys$', 'ies', raw_plural)

    return clean_plural
