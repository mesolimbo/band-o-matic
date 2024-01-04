from randomizer.generators.abstract_generator import AbstractGenerator


class LeaderGenerator(AbstractGenerator):
    def generate_name(self):

        leader = self.util.random_word('Famous')
        adjective = self.util.random_word('Adjective')
        plural_noun = self.util.pluralize(self.util.random_word('Noun'))

        return f"{leader} & The {adjective} {plural_noun}"
