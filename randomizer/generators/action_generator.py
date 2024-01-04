import random
from randomizer.generators.abstract_generator import AbstractGenerator


class ActionGenerator(AbstractGenerator):
    def generate_name(self):
        glue = random.choice(["Can", "Can't", "Will", "Won't", "Might", "Who", "Don't"])
        plural_noun = self.util.pluralize(self.util.random_word('Noun'))
        verb = self.util.random_word('Verb')

        return f"{plural_noun} {glue} {verb}"
