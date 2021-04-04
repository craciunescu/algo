"""
    @author: David E. Craciunescu
      @date: 2020/02/17 (yyyy/mm/dd)

    5. Program a function to determine if a number received as a parameter is
    prime. Analyze the efficiency and complexity of the provided solution(s).
"""
# Testing
import unittest
from U1.src.e5 import is_prime_naive, is_prime_optimized

class TestPrimeMethods(unittest.TestCase):
    """ Test Methods in craciunescu@github.com/algo/U1/src/e5.py """

    # Test is_prime_naive
    def test_is_prime_naive01(self):
        """ Test is_prime_naive """
        self.assertTrue(is_prime_naive(797581))

    def test_is_prime_naive02(self):
        """ Test is_prime_naive """
        self.assertTrue(is_prime_naive(1049))

    def test_is_prime_naive03(self):
        """ Test is_prime_naive """
        self.assertTrue(is_prime_naive(23))

    def test_is_prime_naive04(self):
        """ Test is_prime_naive """
        self.assertTrue(is_prime_naive(2))

    def test_is_prime_naive05(self):
        """ Test is_prime_naive """
        self.assertFalse(is_prime_naive(7917))

    def test_is_prime_naive06(self):
        """ Test is_prime_naive """
        self.assertFalse(is_prime_naive(797582))

    def test_is_prime_naive07(self):
        """ Test is_prime_naive """
        self.assertFalse(is_prime_naive(-4))

    def test_is_prime_naive08(self):
        """ Test is_prime_naive """
        self.assertFalse(is_prime_naive(0))

    # Test is_prime_optimized
    def test_is_prime_optimized01(self):
        """ Test is_prime_optimized """
        self.assertTrue(is_prime_optimized(797581))

    def test_is_prime_optimized02(self):
        """ Test is_prime_optimized """
        self.assertTrue(is_prime_optimized(1049))

    def test_is_prime_optimized03(self):
        """ Test is_prime_optimized """
        self.assertTrue(is_prime_optimized(23))

    def test_is_prime_optimized04(self):
        """ Test is_prime_optimized """
        self.assertTrue(is_prime_optimized(2))

    def test_is_prime_optimized05(self):
        """ Test is_prime_optimized """
        self.assertFalse(is_prime_optimized(7917))

    def test_is_prime_optimized06(self):
        """ Test is_prime_optimized """
        self.assertFalse(is_prime_optimized(797582))

    def test_is_prime_optimized07(self):
        """ Test is_prime_optimized """
        self.assertFalse(is_prime_optimized(-4))

    def test_is_prime_optimized08(self):
        """ Test is_prime_optimized """
        self.assertFalse(is_prime_optimized(0))

if __name__ == '__main__':
    unittest.main()
