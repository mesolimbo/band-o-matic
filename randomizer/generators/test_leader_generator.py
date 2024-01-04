import unittest
from unittest.mock import patch
from randomizer.generators.leader_generator import LeaderGenerator


class TestLeaderGenerator(unittest.TestCase):

    @patch.object(LeaderGenerator, 'util', create=True)
    def test_generate_name(self, mock_util):
        mock_util.random_word.side_effect = ["Famous", "Adjective", "Noun"]
        mock_util.pluralize.return_value = "Nouns"

        leader_generator = LeaderGenerator()

        expected_result = "Famous & The Adjective Nouns"
        result = leader_generator.generate_name()

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
