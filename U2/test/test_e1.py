"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    1. For an even-length non-empty array of non-repeating
    pseudo-randomly-generated positive integer values, form unique pairs between
    such values and return the pair that yields the highest result when both its
    numbers are added together.

    Design a voracious algorithm that creates pairs in such a way that the
    maximum value of the sums is the smallest biggest sum possible, showing that
    candidate selection function used provides an optimal solution.
"""
# Testing
import unittest
from src import e1

class TestMinPairMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e1.py """

    def test_get_min_pair_sum(self):
        """ Test get_min_pair_sum """
        self.assertTrue(e1.get_min_pair_sum([5, 8, 4, 1, 7, 9]))

if __name__ == '__main__':
    unittest.main()
