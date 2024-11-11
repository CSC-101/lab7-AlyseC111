import unittest
import convert


class MyTestCase(unittest.TestCase):

    def test_str_to_float_1(self):
        input = "45.3"
        expected = 45.3
        actual = convert.str_to_float(input)
        self.assertEqual(expected, actual)  # add assertion here
    def test_str_to_float_2(self):
        input = "dog"
        expected = None
        actual = convert.str_to_float(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
