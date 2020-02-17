"""
    @author: David E. Craciunescu
      @date: 2020/02/17 (yyyy/mm/dd)

    5. Program a function to determine if a number received as a parameter is
    prime. Analyze the efficiency and complexity of the provided solution(s).
"""

# Benchmark imports.
import unittest
import sys
sys.path.insert(1, '../src')
import e5.is_prime_naive
from time import time

class TestPrimeMethods(unittest.TestCase):
    """ Test Methods in craciunescu@github.com/algo/U1/src/e5.py """

    def test_is_prime_naive(self):
        self.assertTrue(is_prime_naive(797581))

