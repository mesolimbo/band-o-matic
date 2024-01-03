
import random

from randomizer.generators.abstract_generator import AbstractGenerator


class ShortGenerator(AbstractGenerator):
    def generate_name(self):
        name = []
        if random.randint(1, 100) < 90:
            name.append('The')
        name.append(self.util.pluralize(self.util.random_word('Noun')))

        return ' '.join(name)
