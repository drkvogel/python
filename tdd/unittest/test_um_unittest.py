import unittest
# from tdd.unittest.unnecessary_math import multiply
from unnecessary_math import multiply

class TestUM(unittest.TestCase):

    def setUp(self):
        # return super().setUp()
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')


if __name__ == '__main__':
    unittest.main()
