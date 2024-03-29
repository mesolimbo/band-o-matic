from grammar import plural

class LeaderGeneratorHelper:

    @staticmethod
    def assemble_name(*args):
        famous, adjective, noun = args
        plural_noun = plural(noun)
        return f"{famous} & The {adjective} {plural_noun}"
