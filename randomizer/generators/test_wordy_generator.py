import unittest
from unittest.mock import Mock, call, patch

from randomizer.generators.wordy_generator import WordyGenerator


class TestWordyGenerator(unittest.TestCase):
    def test_generate_name(self):
        # Mock the `self.util` object. This makes the test deterministic.
        util_mock = Mock()
        util_mock.random_word.side_effect = lambda category: f'{category}_word'
        util_mock.pluralize.side_effect = lambda word: f'{word}s'

        # Create WordyGenerator instance with the mocked util assigned to its attribute
        with patch.object(WordyGenerator, "util", util_mock):
            # Instantiate the WordyGenerator with the mocked utility object
            generator = WordyGenerator()

            # Call the method under test
            name = generator.generate_name()

            # Verify the results
            assert name == 'The Adverb_word Adjective_word Noun_words'

            # Verify that the mocked methods were called with the expected arguments
            util_mock.random_word.assert_has_calls([call('Adverb'), call('Adjective'), call('Noun')])
            util_mock.pluralize.assert_called_once_with('Noun_word')


if __name__ == "__main__":
    unittest.main()