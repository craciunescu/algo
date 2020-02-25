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

    # Test is_perfect_naive
    def test_is_perfect_naive01(self):
        """ Test is_perfect_naive """
        self.assertTrue(e6.is_perfect_naive(6))

    def test_is_perfect_naive02(self):
        """ Test is_perfect_naive """
        self.assertTrue(e6.is_perfect_naive(28))

    def test_is_perfect_naive03(self):
        """ Test is_perfect_naive """
        self.assertTrue(e6.is_perfect_naive(496))

    def test_is_perfect_naive04(self):
        """ Test is_perfect_naive """
        self.assertTrue(e6.is_perfect_naive(8128))

    def test_is_perfect_naive05(self):
        """ Test is_perfect_naive """
        self.assertFalse(e6.is_perfect_naive(4))

    def test_is_perfect_naive06(self):
        """ Test is_perfect_naive """
        self.assertFalse(e6.is_perfect_naive(9002))

    def test_is_perfect_naive07(self):
        """ Test is_perfect_naive """
        self.assertFalse(e6.is_perfect_naive(30000))

    def test_is_perfect_naive08(self):
        """ Test is_perfect_naive """
        self.assertFalse(e6.is_perfect_naive(123456))

    # Test is_perfect_optimized
    def test_is_perfect_optimized01(self):
        """ Test is_perfect_optimized """
        self.assertTrue(e6.is_perfect_optimized(6))

    def test_is_perfect_optimized02(self):
        """ Test is_perfect_optimized """
        self.assertTrue(e6.is_perfect_optimized(28))

    def test_is_perfect_optimized03(self):
        """ Test is_perfect_optimized """
        self.assertTrue(e6.is_perfect_optimized(496))

    def test_is_perfect_optimized04(self):
        """ Test is_perfect_optimized """
        self.assertTrue(e6.is_perfect_optimized(8128))

    def test_is_perfect_optimized05(self):
        """ Test is_perfect_optimized """
        self.assertFalse(e6.is_perfect_optimized(4))

    def test_is_perfect_optimized06(self):
        """ Test is_perfect_optimized """
        self.assertFalse(e6.is_perfect_optimized(9002))

    def test_is_perfect_optimized07(self):
        """ Test is_perfect_optimized """
        self.assertFalse(e6.is_perfect_optimized(30000))

    def test_is_perfect_optimized08(self):
        """ Test is_perfect_optimized """
        self.assertFalse(e6.is_perfect_optimized(123456))

if __name__ == '__main__':
    unittest.main()
