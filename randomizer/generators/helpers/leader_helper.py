from randomizer import grammar

class LeaderGeneratorHelper:

    @staticmethod
    def assemble_name(*args):
        famous, adjective, noun = args
        plural_noun = grammar.plural(noun)
        return f"{famous} & The {adjective} {plural_noun}"
