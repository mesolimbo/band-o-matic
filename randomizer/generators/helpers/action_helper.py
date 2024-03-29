import random

from grammar import plural


class ActionGeneratorHelper:
    @staticmethod
    def assemble_name(*args):
        glue = random.choice(["Can", "Can't", "Will", "Won't", "Might", "Who", "Don't"])
        noun, verb = args
        plural_noun = plural(noun)
        return f'{plural_noun} {glue} {verb}'
