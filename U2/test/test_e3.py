"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    3. For a non-emtpy vector of length n, find the minimum and maximum element
    of the vector. The type of data the vector contains is not relevant to the
    problem, but performing comparisons between elements in the vector is an
    extremely expensive operation, so you should minimize the amount of
    comparisons.

    Implement a greedy method that makes a maximum of (3/2)n comparisons.

"""
# Testing
import unittest
from U2.src.e3 import min_and_max

class TestMinMaxMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e3.py """

    def test_min_and_max01(self):
        """ Test min_and_max """
        provided = min_and_max([1, 2, 3, 4, 5])
        expected = [5, 1]

        self.assertEqual(provided, expected)

    def test_min_and_max02(self):
        """ Test min_and_max """
        provided = min_and_max([5, 2, 6, 1, 2, 4, 6])
        expected = [6, 1]

        self.assertEqual(provided, expected)

    def test_min_and_max03(self):
        """ Test min_and_max """
        provided = min_and_max([-1, -5, 2, 2, 4, 5])
        expected = [5, -5]

        self.assertEqual(provided, expected)

    def test_min_and_max04(self):
        """ Test min_and_max """
        provided = min_and_max([])
        expected = []
        
        self.assertEqual(provided, expected)

if __name__ == '__main__':
    unittest.main()
