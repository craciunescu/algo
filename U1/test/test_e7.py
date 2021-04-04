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
from U1.src.e7 import amount_perfects, amount_primes, amount_primes_perfects

class TestCountMethods(unittest.TestCase):
    """ Test Methods in craciunescu@github.com/algo/U1/src/e7.py """

    # Test amount_primes
    def test_amount_primes01(self):
        """ Test amount_primes """
        provided = amount_primes(997)
        expected = 168
        self.assertEqual(provided, expected)

    def test_amount_primes02(self):
        """ Test amount_primes """
        provided = amount_primes(461)
        expected = 89
        self.assertEqual(provided, expected)

    def test_amount_primes03(self):
        """ Test amount_primes """
        provided = amount_primes(547)
        expected = 101
        self.assertEqual(provided, expected)

    def test_amount_primes04(self):
        """ Test amount_primes """
        provided = amount_primes(59)
        expected = 17
        self.assertEqual(provided, expected)

    # Test amount_perfects
    def test_amount_perfects01(self):
        """ Test amount_perfects """
        provided = amount_perfects(6)
        expected = 1
        self.assertEqual(provided, expected)

    def test_amount_perfects02(self):
        """ Test amount_perfects """
        provided = amount_perfects(28)
        expected = 2
        self.assertEqual(provided, expected)
        
    def test_amount_perfects03(self):
        """ Test amount_perfects """
        provided = amount_perfects(496)
        expected = 3
        self.assertEqual(provided, expected)
        
    def test_amount_perfects04(self):
        """ Test amount_perfects """
        provided = amount_perfects(8128)
        expected = 4
        self.assertEqual(provided, expected)

    # Test amount_primes_perfects
    def test_amount_perfect_primes01(self):
        """ Test amount_perfect_primes """
        provided = amount_primes_perfects(997)
        expected = (168, 3)
        self.assertEqual(provided, expected)

    def test_amount_perfect_primes02(self):
        """ Test amount_perfect_primes """
        provided = amount_primes_perfects(461)
        expected = (89, 2)
        self.assertEqual(provided, expected)

if __name__ == '__main__':
    unittest.main()
