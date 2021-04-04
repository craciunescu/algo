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
from U2.src.e1 import get_min_pair_sum

class TestMinPairMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e1.py """

    def test_get_min_pair_sum01(self):
        """ Test get_min_pair_sum """
        provided = get_min_pair_sum([5, 8, 4, 1, 7, 9])
        expected = 12

        self.assertEqual(provided, expected)

    def test_get_min_pair_sum02(self):
        """ Test get_min_pair_sum """
        provided = get_min_pair_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected = 11

        self.assertEqual(provided, expected)

    def test_get_min_pair_sum03(self):
        """ Test get_min_pair_sum """
        provided = get_min_pair_sum([7, 7, 7, 7, 7, 7])
        expected = 14

        self.assertEqual(provided, expected)

    def test_get_min_pair_sum04(self):
        """ Test get_min_pair_sum """
        provided = get_min_pair_sum([1000, 1, 1234, 3, 23455, 4, 6666, 9])
        expected = 23456
        
        self.assertEqual(provided, expected)

if __name__ == '__main__':
    unittest.main()
