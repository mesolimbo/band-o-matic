import unittest
from unittest import mock

from randomizer.picker import generate_band_name, GENERATORS


class TestPicker(unittest.TestCase):
    @mock.patch("random.choice", return_value=mock.MagicMock())
    def test_generate_band_name(self, mock_choice):
        mock_choice.return_value.generate_name.return_value = "Test Band Name"

        result = generate_band_name()

        self.assertEqual(result, "Test Band Name")
        mock_choice.assert_called_once_with(GENERATORS)


if __name__ == "__main__":
    unittest.main()