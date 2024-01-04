import unittest
from unittest.mock import patch

from randomizer.generators.action_generator import ActionGenerator  # replace this with actual module path


class TestActionGenerator(unittest.TestCase):
    @patch('random.choice', return_value="Can")  # replace this with real module path
    @patch('randomizer.generators.action_generator.ActionGenerator.util')
    def test_generate_name(self, util_mock, random_mock):
        # Set up the mocks
        util_mock.pluralize.return_value = "Cats"
        util_mock.random_word.side_effect = ["Noun", "Verb"]

        # Create an instance of the class
        generator = ActionGenerator()

        # Call the method to test
        result = generator.generate_name()

        # Check the result
        self.assertEqual(result, "Cats Can Verb")

        # Check if the mocks were called correctly
        util_mock.pluralize.assert_called_once_with("Noun")
        util_mock.random_word.assert_any_call('Noun')
        util_mock.random_word.assert_any_call('Verb')
        random_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
