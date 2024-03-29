import random
import time

from randomizer.generators.abstract_generator import AbstractGenerator
from randomizer.generators.helpers.combo_helper import ComboGeneratorHelper


class ComboGenerator(AbstractGenerator):

    def __init__(self):
        super().__init__()
        # Setting the seed with the epoch time ensures a new seed with each instantiation
        random.seed(time.time())

    def generate_name(self):
        noun1 = self.util.random_word('Noun')
        noun2 = self.util.random_word('Noun')

        while noun1 == noun2:
            noun2 = self.util.random_word('Noun')

        return ComboGeneratorHelper.assemble_name(noun1, noun2)
