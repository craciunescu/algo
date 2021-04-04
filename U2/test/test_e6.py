"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    6. Shrek, Donkey and Dragona have just arrived to the base of Lord
    Farquaad's towering castle determined to free Fiona from her confinement. As
    they suspected, the drawbridge is guarded by multiple soldiers. Worry not,
    for they suspected such a thing could happen and carried with them a huge
    amount of ladders of all kinds and lengths so that they could get over the
    wall easily.

    (...)

    Analyze the efficiency and complexity of the provided solution.
"""
# Testing
import unittest
from U2.src.e6 import minimum_sum

class TestMinimumSumMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e6.py """

    def test_minimum_sum01(self):
        """ Test minimum_sum """
        provided = minimum_sum([1, 2, 3, 4, 5])
        expected = 33

        self.assertEqual(provided, expected)

    def test_minimum_sum02(self):
        """ Test minimum_sum """
        provided = minimum_sum([])
        expected = 0

        self.assertEqual(provided, expected)

    def test_minimum_sum03(self):
        """ Test minimum_sum """
        provided = minimum_sum([-1, -1, -1, -1, -1])
        expected = -14

        self.assertEqual(provided, expected)

    def test_minimum_sum04(self):
        """ Test minimum_sum """
        provided = minimum_sum([0, 0, 0, 0, 13])
        expected = 13
        
        self.assertEqual(provided, expected)

if __name__ == '__main__':
    unittest.main()
