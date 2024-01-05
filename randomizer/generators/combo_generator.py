import random
import time

from randomizer.generators.abstract_generator import AbstractGenerator


class ComboGenerator(AbstractGenerator):
    def __init__(self):
        super().__init__()
        self.prefixes = ["The", "My", "This", "His", "Her", "Their", "Our"]
        # Setting the seed with the epoch time ensures a new seed with each instantiation
        random.seed(time.time())

    def generate_name(self):
        prefix1 = random.choice(self.prefixes)
        noun1 = self.util.random_word('Noun')

        prefix2 = random.choice(self.prefixes)
        noun2 = self.util.random_word('Noun')

        while noun1 == noun2:
            noun2 = self.util.random_word('Noun')

        return f"{prefix1} {noun1} & {prefix2} {noun2}"
