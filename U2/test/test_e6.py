"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    6. Shrek, Donkey and Dragona have just arrived to the base of Lord
    Farquaad's towering castle determined to free Fiona from her confinement. As
    they suspected, the drawbridge is guarded by multiple soldiers. Worry not,
    for they suspected such a thing could happen and carried with them a huge
    amount of ladders of all kinds and lengths so that they could get over the
    wall easily.

    Unfortunately, no ladder would be enough for them to get over the wall.
    Dragona is also unable to fly that high, so they seemed to be stuck at
    first. But just when they were about to give up, Shrek realized that the
    ladders they brought with them were all made of iron, which could be easily
    welded by Dragona's fire.

    She can weld any two ladders with her fire breath, but the time it takes for
    them to be completely welded is equal to the sum of their length. For
    example, welding a 6-meter ladder and an 8-meter one would take 6+8 = 14
    units of time. If this ladder were then welded to a 7-meter ladder, the time
    it would take to weld them would be 14+7 = 21 units of time. With this
    approach, it would have taken 14+21 = 35 units of time to complete the
    ladder.

    Design an efficient algorithm that finds the best cost and way to weld the
    stairs so that Shrek takes as little time as possible to get past the wall.
    Indicate the data structures that were used to solve this exercise and
    justify their use. Assume the set of ladders they have always contains only
    the exact amount of ladders needed to get past the wall.

    Analyze the efficiency and complexity of the provided solution.
"""
# Testing
import unittest
from src import e6

class TestMinimumSumMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e6.py """

    def test_minimum_sum01(self):
        """ Test minimum_sum """
        self.assertEqual(e6.minimum_sum([1, 2, 3, 4, 5]), 33)

    def test_minimum_sum02(self):
        """ Test minimum_sum """
        self.assertEqual(e6.minimum_sum([]), 0)

    def test_minimum_sum03(self):
        """ Test minimum_sum """
        self.assertEqual(e6.minimum_sum([-1, -1, -1, -1, -1]), -14)

    def test_minimum_sum04(self):
        """ Test minimum_sum """
        self.assertEqual(e6.minimum_sum([0, 0, 0, 0, 13]), 13)

if __name__ == '__main__':
    unittest.main()
