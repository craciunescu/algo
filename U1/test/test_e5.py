"""
    @author: David E. Craciunescu
      @date: 2020/02/17 (yyyy/mm/dd)

    5. Program a function to determine if a number received as a parameter is
    prime. Analyze the efficiency and complexity of the provided solution(s).
"""
# Benchmarking
from time import time

# Testing
import unittest
from src import e5

class TestPrimeMethods(unittest.TestCase):
    """ Test Methods in craciunescu@github.com/algo/U1/src/e5.py """

    def test_is_prime_naive(self):
        """ Test is_prime_naive """
        self.assertTrue(e5.is_prime_naive(797581))
        self.assertTrue(e5.is_prime_naive(1049))
        self.assertTrue(e5.is_prime_naive(23))
        self.assertTrue(e5.is_prime_naive(2))

        self.assertFalse(e5.is_prime_naive(7917))
        self.assertFalse(e5.is_prime_naive(797582))
        self.assertFalse(e5.is_prime_naive(-4))
        self.assertFalse(e5.is_prime_naive(0))
        self.assertFalse(e5.is_prime_naive(24))

    def test_is_prime_optimized(self):
        """ Test is_prime_optimized """

        self.assertTrue(e5.is_prime_optimized(797581))
        self.assertTrue(e5.is_prime_optimized(1049))
        self.assertTrue(e5.is_prime_optimized(23))
        self.assertTrue(e5.is_prime_optimized(2))

        self.assertFalse(e5.is_prime_optimized(7917))
        self.assertFalse(e5.is_prime_optimized(797582))
        self.assertFalse(e5.is_prime_optimized(-4))
        self.assertFalse(e5.is_prime_optimized(0))
        self.assertFalse(e5.is_prime_optimized(24))

if __name__ == '__main__':
    unittest.main()
