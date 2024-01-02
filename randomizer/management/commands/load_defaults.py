from csv import DictReader

from django.core.management import BaseCommand

from randomizer.models import Word, Category, WordCategory

CATEGORIES = [
    'Adjective',
    'Adverb',
    'Noun',
    'Famous',
    'Verb',
]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the Word defaults from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    """To load default words, run command from the project root: `./manage.py load_defaults`"""
    # Show this when the user types help
    help = "Loads default words from defaut_words.csv into our Word model"

    def handle(self, *args, **options):
        if Category.objects.exists() or Word.objects.exists():
            print('Default data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        # print("Creating Category data")
        # for category_name in CATEGORIES:
        #     cat = Category(name=category_name)
        #     cat.save()
        print("Loading default Word and Category defaults")
        for row in DictReader(open('./defaut_words.csv')):
            # First, create or retrieve a category
            category, _ = Category.objects.get_or_create(name=row['category'])

            # Next, create or retrieve a word
            word, _ = Word.objects.get_or_create(name=row['name'])

            # Finally, create or retrieve a new WordCategory instance to link the word and category
            word_category, _ = WordCategory.objects.get_or_create(
                word=word, category=category
            )
