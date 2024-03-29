import random
import time

from randomizer.generators.abstract_generator import AbstractGenerator
from awslambda.helpers.action_helper import ActionGeneratorHelper


class ActionGenerator(AbstractGenerator):
    def __init__(self):
        super().__init__()
        # Setting the seed with the epoch time ensures a new seed with each instantiation
        random.seed(time.time())

    def generate_name(self):
        noun = self.util.random_word('Noun')
        verb = self.util.random_word('Verb')

        return ActionGeneratorHelper.assemble_name(noun, verb)
