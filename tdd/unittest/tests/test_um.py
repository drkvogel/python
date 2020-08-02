import unittest
# from tdd.unittest.unnecessary_math import multiply
from unnecessary_math import multiply

class TestUM(unittest.TestCase):

    def setUp(self):
        # return super().setUp()
        pass

    def test_numbers_5_6(self):
        self.assertEqual(multiply(5, 6), 30)

    def test_strings_b_4(self):
        self.assertEqual(multiply('b', 4), 'bbbb')


if __name__ == '__main__':
    unittest.main()
