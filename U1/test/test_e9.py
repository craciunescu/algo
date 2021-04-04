"""
    @author: David E. Craciunescu
      @date: 2020/02/18 (yyyy/mm/dd)

    9. Program a recursive function to calculate the following sum:
    S = 1 + 2 + 3 + 4 + (...) + n-1 + n.
    Analyze the efficiency and complexity of the provided solution.
"""
# Testing
import unittest
from U1.src.e9 import summation

class TestSummationMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U1/src/e9.py """

    # Test summation
    def test_summation01(self):
        """ Test summation """
        provided = summation(10)
        expected = sum(range(10+1))
        self.assertEqual(provided, expected)

    def test_summation02(self):
        """ Test summation """
        provided = summation(100)
        expected = sum(range(100+1))
        self.assertEqual(provided, expected)

    def test_summation03(self):
        """ Test summation """
        provided = summation(300)
        expected = sum(range(300+1))
        self.assertEqual(provided, expected)

if __name__ == '__main__':
    unittest.main()
