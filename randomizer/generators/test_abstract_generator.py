import unittest

from randomizer.generators.abstract_generator import AbstractGenerator


class TestAbstractGenerator(unittest.TestCase):
    def test_instantiation(self):
        with self.assertRaises(TypeError):
            AbstractGenerator()


if __name__ == '__main__':
    unittest.main()
