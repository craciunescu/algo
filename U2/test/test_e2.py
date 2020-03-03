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

def generate_vector(seed):
    """ Generate a test vector """
    r.seed(a=seed)
    max_len = r.randint(1, 10)
    return [[r.randint(1, 100), r.randint(1, 100)] for num in range(1, max_len)]

def test_general(vector):
    """ Generate vector permutations and return minimum cost """
    perms = list(permutations(vector))
    return min([calculate_cost(perm) for perm in perms])

class TestStoreFilesMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e2.py """

    def test_store_files01(self):
        """ Test store_files """
        test_vector = generate_vector("test_store_files01")
        min_value = test_general(test_vector)
        self.assertEqual(calculate_cost(e2.store_files(test_vector)), min_value)

    def test_store_files02(self):
        """ Test store_files """
        test_vector = generate_vector("test_store_files02")
        min_value = test_general(test_vector)
        self.assertEqual(calculate_cost(e2.store_files(test_vector)), min_value)

    def test_store_files03(self):
        """ Test store_files """
        test_vector = generate_vector("test_store_files03")
        min_value = test_general(test_vector)
        self.assertEqual(calculate_cost(e2.store_files(test_vector)), min_value)

    def test_store_files04(self):
        """ Test store_files """
        test_vector = generate_vector("test_store_files04")
        min_value = test_general(test_vector)
        self.assertEqual(calculate_cost(e2.store_files(test_vector)), min_value)

if __name__ == "__main__":
    unittest.main()
