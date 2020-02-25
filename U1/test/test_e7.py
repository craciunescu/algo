"""
    @author: David E. Craciunescu
      @date: 2020/02/18 (yyyy/mm/dd)

    7. Write a program which asks the user for a positive number N and obtains
    the amount of prime numbers and the amount of perfect numbers there are
    between 1 and N. Analyze the efficiency and complexity of the provided
    solution.
"""
# Testing
import unittest
from src import e7

class TestCountMethods(unittest.TestCase):
    """ Test Methods in craciunescu@github.com/algo/U1/src/e7.py """

    # Test amount_primes
    def test_amount_primes01(self):
        """ Test amount_primes """
        self.assertEqual(e7.amount_primes(997), 168)

    def test_amount_primes02(self):
        """ Test amount_primes """
        self.assertEqual(e7.amount_primes(461), 89)

    def test_amount_primes03(self):
        """ Test amount_primes """
        self.assertEqual(e7.amount_primes(547), 101)

    def test_amount_primes04(self):
        """ Test amount_primes """
        self.assertEqual(e7.amount_primes(59), 17)

    # Test amount_perfects
    def test_amount_perfects01(self):
        """ Test amount_perfects """
        self.assertEqual(e7.amount_perfects(6), 1)

    def test_amount_perfects02(self):
        """ Test amount_perfects """
        self.assertEqual(e7.amount_perfects(28), 2)
        
    def test_amount_perfects03(self):
        """ Test amount_perfects """
        self.assertEqual(e7.amount_perfects(496), 3)
        
    def test_amount_perfects04(self):
        """ Test amount_perfects """
        self.assertEqual(e7.amount_perfects(8128), 4)

if __name__ == '__main__':
    unittest.main()
