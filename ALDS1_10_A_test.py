import unittest

from ALDS1_10_A import fib


class TestFib(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(0), 1)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 2)
        self.assertEqual(fib(3), 3)
        self.assertEqual(fib(4), 5)


if __name__ == "__main__":
    unittest.main()
