"""
    @author: David E. Craciunescu
      @date: 2020/02/25 (yyyy/mm/dd)

    2. A set of n files must be stored on a magnetic tape (sequential path)
"""
# Testing
import unittest
import random as r
from itertools import permutations
from src import e2

def calculate_cost(files):
    """ Calculate the cost associated with a possible solution """
    offset = 0
    cost = 0

    for file in files:
        cost = (offset + file[0]) * file[1]
        offset += file[0]

    return cost

class TestStoreFilesMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e2.py """

    def test_general(self, seed):
        """ Test store_files """
        r.seed(a=seed)
        max_len = r.randint(0, 10)
        vector = [[r.randint(0, 100), r.randint(0, 100)] for num in range(1, max_len)]

        perms = list(permutations(vector))
        min_cost = min([calculate_cost(perm) for perm in perms])

        self.assertEqual(calculate_cost(e2.store_files(vector)), min_cost)

    def test_store_files01(self):
        """ Test store_files """
        self.test_general("test_store_files01")

    def test_store_files02(self):
        """ Test store_files """
        self.test_general("test_store_files02")

    def test_store_files03(self):
        """ Test store_files """
        self.test_general("test_store_files03")

    def test_store_files04(self):
        """ Test store_files """
        self.test_general("test_store_files04")

if __name__ == "__main__":
    unittest.main()
