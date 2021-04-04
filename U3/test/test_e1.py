"""
    @author: David E. Craciunescu
      @date: 2021/04/01 (yyyy/mm/dd)

    1. For a non-empty vector of non-repeating pseudo-randomly-generated
    integer values ordered in increasing order, design a divide-and-conquer
    algorithm that finds if the vector is coincident.
"""
# Testing
import unittest
from U3.src.e1 import coincident

class TestMinPairMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U3/src/e1.py """

    def test_coincident01(self):
        """ Test coincident """
        provided = coincident([5, 8, 4, 1, 7, 9])
        self.assertFalse(provided)

    def test_coincident02(self):
        """ Test coincident """
        provided = coincident([0, 1, 2, 3, 4])
        self.assertTrue(provided)

    def test_coincident03(self):
        """ Test coincident """
        provided = coincident([])
        self.assertFalse(provided)

if __name__ == '__main__':
    unittest.main()
