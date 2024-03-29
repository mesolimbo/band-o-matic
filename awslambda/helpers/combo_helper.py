import random


class ComboGeneratorHelper:
    prefixes = ["The", "My", "This", "His", "Her", "Their", "Our"]

    @staticmethod
    def assemble_name(*args):
        noun1, noun2 = args
        prefix1 = random.choice(ComboGeneratorHelper.prefixes)
        prefix2 = random.choice(ComboGeneratorHelper.prefixes)
        return f'{prefix1} {noun1} & {prefix2} {noun2}'
