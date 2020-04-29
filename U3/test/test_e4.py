"""
    @author: David E. Craciunescu
      @date: 2020/04/29 (yyyy/mm/dd)

    4. You'd like to program a robot to match cork stoppers to glass bottles at
    a recyling factory.

    Design an algorithm that follows the Divide and Conquer scheme to plug N
    bottles optimally.
"""
from random import randint, shuffle

# Testing
import unittest
from src import e4

class TestMatchMethods(unittest.TestCase):
    """ Test match method in craciunescu@github.com/algo/U3/src/e4.py """

    @staticmethod
    def data_generator(limit):
        """ Generate datasets to test """
        length = randint(1, limit)

        provided1 = list(range(length))
        provided2 = provided1[:]
        expect = zip(provided1, provided2)

        shuffle(provided1)
        shuffle(provided2)

        return (provided1, provided2, expect)

    def test_match01(self):
        """ Test match 01 """
        set1, set2, exp = self.data_generator(100)
        self.assertEqual(e4.match(set1, set2), exp)

    def test_match02(self):
        """ Test match 02 """
        set1, set2, exp = self.data_generator(1000)
        self.assertEqual(e4.match(set1, set2), exp)

    def test_match03(self):
        """ Test match 03 """
        set1, set2, exp = self.data_generator(10000)
        self.assertEqual(e4.match(set1, set2), exp)

    def test_match04(self):
        """ Test match 04 """
        set1, set2, exp = self.data_generator(100000)
        self.assertEqual(e4.match(set1, set2), exp)

if __name__ == '__main__':
    unittest.main()
