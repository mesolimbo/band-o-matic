import random
import time

from randomizer.generators.abstract_generator import AbstractGenerator
from randomizer.generators.helpers.short_helper import ShortGeneratorHelper


class ShortGenerator(AbstractGenerator):
    def __init__(self):
        super().__init__()
        # Setting the seed with the epoch time ensures a new seed with each instantiation
        random.seed(time.time())

    def generate_name(self):
        noun = self.util.random_word('Noun')

        # return ' '.join(name)
        return ShortGeneratorHelper.assemble_name(noun)
