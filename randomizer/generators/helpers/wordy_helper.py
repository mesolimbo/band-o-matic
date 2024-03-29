class WordyGeneratorHelper:

    @staticmethod
    def assemble_name(*args):
        adverb, adjective, noun = args
        return f'The {adverb} {adjective} {noun}'
