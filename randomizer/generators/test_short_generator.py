import unittest
from unittest.mock import patch, MagicMock

from randomizer.generators.short_generator import ShortGenerator


class TestShortGenerator(unittest.TestCase):
    def setUp(self):  # setUp will be called before each test
        self.obj = ShortGenerator()
        self.obj.util = MagicMock()

    @patch("random.randint", return_value=90)
    def test_generate_name_greater_than_90(self, _):
        self.obj.util.pluralize.return_value = "Tests"
        self.obj.util.random_word.return_value = "Test"
        self.assertEqual(self.obj.generate_name(), "Tests")

    @patch("random.randint", return_value=89)
    def test_generate_name_less_than_90(self, _):
        self.obj.util.pluralize.return_value = "Tests"
        self.obj.util.random_word.return_value = "Test"
        self.assertEqual(self.obj.generate_name(), "The Tests")


if __name__ == "__main__":
    unittest.main()