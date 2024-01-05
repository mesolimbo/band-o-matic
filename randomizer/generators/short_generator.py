import random
import time

from randomizer.generators.abstract_generator import AbstractGenerator


class ShortGenerator(AbstractGenerator):
    def __init__(self):
        super().__init__()
        # Setting the seed with the epoch time ensures a new seed with each instantiation
        random.seed(time.time())

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
