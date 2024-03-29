import random
from randomizer import grammar


class ShortGeneratorHelper:

    @staticmethod
    def assemble_name(*args):
        noun, = args
        name = []
        if random.randint(1, 100) < 80:
            name.append('The')
        if random.randint(1, 100) < 30:
            name.append(str(noun))
        else:
            name.append(grammar.plural(noun))
        return ' '.join(name)
