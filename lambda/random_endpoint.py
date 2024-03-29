import random
import boto3
from boto3.dynamodb.conditions import Attr

from randomizer.generators.helpers.action_helper import ActionGeneratorHelper
from randomizer.generators.helpers.combo_helper import ComboGeneratorHelper
from randomizer.generators.helpers.leader_helper import LeaderGeneratorHelper
from randomizer.generators.helpers.short_helper import ShortGeneratorHelper
from randomizer.generators.helpers.wordy_helper import WordyGeneratorHelper

# Set up DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bandomatic_Words')


# Function to fetch a random word from DynamoDB based on the category
def random_word(category):
    response = table.scan(
        FilterExpression=Attr('category_ids').contains(category)
    )
    words = response['Items']
    return random.choice(words)['name']


class ActionGeneratorLambda:
    @staticmethod
    def generate_name():
        noun = random_word('Noun')
        verb = random_word('Verb')

        return ActionGeneratorHelper.assemble_name(noun, verb)


class ComboGeneratorLambda:
    @staticmethod
    def generate_name():
        noun1 = random_word('Noun')
        noun2 = random_word('Noun')
        return ComboGeneratorHelper.assemble_name(noun1, noun2)


class LeaderGeneratorLambda:
    @staticmethod
    def generate_name():
        famous = random_word('Famous')
        adjective = random_word('Adjective')
        noun = random_word('Noun')

        return LeaderGeneratorHelper.assemble_name(famous, adjective, noun)


class ShortGeneratorLambda:
    @staticmethod
    def generate_name():
        return ShortGeneratorHelper.assemble_name(random_word('Noun'))


class WordyGeneratoLambda:
    @staticmethod
    def generate_name():
        adverb = random_word('Adverb')
        adjective = random_word('Adjective')
        noun = random_word('Noun')

        return WordyGeneratorHelper.assemble_name(adverb, adjective, noun)


# Function to randomly select a generator and generate a name
def generate_band_name():
    generators = [
        ActionGeneratorLambda, ComboGeneratorLambda, LeaderGeneratorLambda, ShortGeneratorLambda, WordyGeneratoLambda]
    generator = random.choice(generators)()
    return generator.generate_name()


# AWS Lambda handler function
def lambda_handler(event, context):
    band_name = generate_band_name()
    return {
        'band_name': band_name
    }


if __name__ == '__main__':
    print(lambda_handler(None, None))
