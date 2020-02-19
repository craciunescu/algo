"""
    @author: David E. Craciunescu
      @date: 2020/02/18 (yyyy/mm/dd)

    9. Program a recursive function to calculate the following sum:
    S = 1 + 2 + 3 + 4 + (...) + n-1 + n.
    Analyze the efficiency and complexity of the provided solution.
"""
# Testing
import unittest
from src import e9

class TestSummationMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U1/src/e9.py """

    def test_summation(self):
        """ Test summation """
        self.assertEqual(e9.summation(10), sum(range(10+1)))
        self.assertEqual(e9.summation(100), sum(range(100+1)))
        self.assertEqual(e9.summation(300), sum(range(300+1)))

if __name__ == '__main__':
    unittest.main()
