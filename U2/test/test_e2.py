"""
    @author: David E. Craciunescu
      @date: 2020/02/25 (yyyy/mm/dd)

    2. A set of n files must be stored on a magnetic tape (sequential path)
"""
# Testing
import unittest
import random as r
from itertools import permutations
from U2.src.e2 import store_files

def calculate_cost(files):
    """ Calculate the cost associated with a possible solution """
    offset = cost = 0

    for file in files:
        cost += (offset + file[0]) * file[1]
        offset += file[0]

    return cost

def generate_test_vector(seed):
    """ Generate a test vector """
    r.seed(a=seed)
    max_len = r.randint(1, 10)
    return [[r.randint(1, 100), r.randint(1, 100)] for _ in range(1, max_len)]

def generate_expected(vector):
    """ Generate vector permutations and return minimum cost possible """
    perms = list(permutations(vector))
    return min([calculate_cost(perm) for perm in perms])

def generate_dataset(seed):
    test_vector = generate_test_vector(seed)
    
    provided = calculate_cost(store_files(test_vector))
    expected = generate_expected(test_vector)

    return (provided, expected)
class TestStoreFilesMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e2.py """

    def test_store_files01(self):
        """ Test store_files """
        provided, expected = generate_dataset("test_store_files01")
        self.assertEqual(provided, expected)

    def test_store_files02(self):
        """ Test store_files """
        provided, expected = generate_dataset("test_store_files02")
        self.assertEqual(provided, expected)

    def test_store_files03(self):
        """ Test store_files """
        provided, expected = generate_dataset("test_store_files03")
        self.assertEqual(provided, expected)

    def test_store_files04(self):
        """ Test store_files """
        provided, expected = generate_dataset("test_store_files04")
        self.assertEqual(provided, expected)

if __name__ == "__main__":
    unittest.main()
