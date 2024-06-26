from randomizer.generators.abstract_generator import AbstractGenerator
from awslambda.helpers.wordy_helper import WordyGeneratorHelper


class WordyGenerator(AbstractGenerator):

    def generate_name(self):
        adverb = self.util.random_word('Adverb')
        adjective = self.util.random_word('Adjective')
        noun = self.util.pluralize(self.util.random_word('Noun'))

        return WordyGeneratorHelper.assemble_name(adverb, adjective, noun)
