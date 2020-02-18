"""
    @author: David E. Craciunescu
      @date: 2020/02/18 (yyyy/mm/dd)

    6. Program a function to determine if a number received as a parameter is
    perfect. Analyze the efficiency and complexity of the provided solution.
"""
# Testing
import unittest
from src import e6

class TestPerfectMethods(unittest.TestCase):
    """ Test Methods in craciunescu@github.com/algo/U1/src/e6.py """

    def test_is_perfect_naive(self):
        """ Test is_perfect_naive """
        self.assertTrue(e6.is_perfect_naive(6))
        self.assertTrue(e6.is_perfect_naive(28))
        self.assertTrue(e6.is_perfect_naive(496))
        self.assertTrue(e6.is_perfect_naive(8128))

        self.assertFalse(e6.is_perfect_naive(4))
        self.assertFalse(e6.is_perfect_naive(9002))
        self.assertFalse(e6.is_perfect_naive(30000))
        self.assertFalse(e6.is_perfect_naive(123456))

    def test_is_perfect_optimized(self):
        """ Test is_perfect_optimized """
        self.assertTrue(e6.is_perfect_optimized(6))
        self.assertTrue(e6.is_perfect_optimized(28))
        self.assertTrue(e6.is_perfect_optimized(496))
        self.assertTrue(e6.is_perfect_optimized(8128))

        self.assertFalse(e6.is_perfect_optimized(4))
        self.assertFalse(e6.is_perfect_optimized(9002))
        self.assertFalse(e6.is_perfect_optimized(30000))
        self.assertFalse(e6.is_perfect_optimized(123456))

if __name__ == '__main__':
    unittest.main()
