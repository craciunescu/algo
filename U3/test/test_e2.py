"""
    @author: David E. Craciunescu
      @date: 2021/03/10 (yyyy/mm/dd)

    2. We are given a vector of unordered positive integers that we cannot alter 
    or copy in any way, shape, or form. Yet, we'd like to obtain information from
    this vector as if it were ordered.

    => Modify the standard MergeSort algorithm in order to obtain the vector
    indices of a vector V[1...N] given as a parameter.
"""
# Testing
import unittest
from src import e2

class TestMergeSortMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U3/src/e2.py """

    def test_merge_sort_index01(self):
        """ Test merge_sort_index """
        self.assertEqual(e2.merge_sort_idx(
            [3, 2, 5, 7, 4, 1, 1],
            [5, 6, 1, 0, 4, 2, 3]
        ))
    
    def test_merge_sort_index02(self):
        """ Test merge_sort_index """
        self.assertEqual(e2.merge_sort_idx(
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 2, 3, 4, 5, 6]
        ))

    def test_merge_sort_index03(self):
        """ Test merge_sort_index """
        self.assertEqual(e2.merge_sort_idx(
            [-3, 2, 1, 7, 0, -4],
            [5, 0, 4, 2, 1, 3]
        ))

    def test_merge_sort_index04(self):
        """ Test merge_sort_index """
        self.assertEqual(e2.merge_sort_idx(
            [],
            []
        ))


if __name__ == '__main__':
    unittest.main()
