import unittest
import unittest.mock as mock

from randomizer.generators.combo_generator import ComboGenerator


class TestComboGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ComboGenerator()

    @mock.patch('random.choice')
    @mock.patch('randomizer.generators.abstract_generator.AbstractGenerator.util')
    def test_generate_name(self, mock_util, mock_choice):
        # Define the return values for the mocks
        mock_util.random_word.side_effect = ["Noun1", "Noun2"]
        mock_choice.side_effect = ["This", "That"]

        # Call the method under test
        result = self.generator.generate_name()

        # Verify the result and interactions
        self.assertListEqual(mock_util.random_word.call_args_list, [mock.call('Noun'), mock.call('Noun')])
        self.assertListEqual(mock_choice.call_args_list, [mock.call(self.generator.prefixes), mock.call(self.generator.prefixes)])
        self.assertEqual(result, "This Noun1 & That Noun2")


if __name__ == "__main__":
    unittest.main()
