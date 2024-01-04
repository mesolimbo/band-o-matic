import random

from randomizer.generators.abstract_generator import AbstractGenerator


class ShortGenerator(AbstractGenerator):
    def generate_name(self):
        name = []
        if random.randint(1, 100) < 80:
            name.append('The')
        noun = self.util.random_word('Noun')
        if random.randint(1, 100) < 30:
            name.append(str(noun))
        else:
            name.append(self.util.pluralize(noun))

        return ' '.join(name)
