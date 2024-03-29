from randomizer.generators.abstract_generator import AbstractGenerator
from awslambda.helpers.leader_helper import LeaderGeneratorHelper


class LeaderGenerator(AbstractGenerator):

    def generate_name(self):

        famous = self.util.random_word('Famous')
        adjective = self.util.random_word('Adjective')
        noun = self.util.random_word('Noun')

        return LeaderGeneratorHelper.assemble_name(famous, adjective, noun)
