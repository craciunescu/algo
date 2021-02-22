"""
    @author: David E. Craciunescu
      @date: 2020/04/30 (yyyy/mm/dd)

    6. After passing through the Tile Room and stealing the Craddle of Life,
    Indiana Croft faces a new challenge before leaving the Cursed Temple! The
    Temple itself is located on a bridge under which there is a deep darkness.

    In order to save our hero, design the algorithm that Indiana Croft should
    use to find the minimum point of the valley under the conditions mentioned
    above. The algorithm must be efficient, for he cannot afford to waste a
    single second: at least in the best case it must have a logarithmic order.
"""
from random import randint
from math import ceil

# Testing
import unittest
from src import e6

class TestGradDescentMethod(unittest.TestCase):
    """ Test grad_descent method in craciunescu@github.com/algo/U3/src/e6.py """

    @staticmethod
    def generate_dataset(error_rate):
        """ Generate dataset to test """

        test_case = [randint(500, 600)]

        for _ in range(randint(5, 10)):
            test_case.append(test_case[-1] - randint(10, 30))
        for _ in range(randint(5, 10)):
            test_case.append(test_case[-1] + randint(10, 30))

        # Allow for error.
        error_window = ceil(len(test_case) * error_rate)
        expected = sorted(test_case[:])
        expected = expected[:error_window]

        return test_case, expected

    def test_grad_descent01(self):
        """ Test grad_descent 01 """
        test_case, expected = self.generate_dataset(0.1)
        self.assertIn(test_case[e6.grad_descent(test_case)], expected)

    def test_grad_descent02(self):
        """ Test grad_descent 02 """
        test_case, expected = self.generate_dataset(0.1)
        self.assertIn(test_case[e6.grad_descent(test_case)], expected)

    def test_grad_descent03(self):
        """ Test grad_descent 03 """
        test_case, expected = self.generate_dataset(0.1)
        self.assertIn(test_case[e6.grad_descent(test_case)], expected)

    def test_grad_descent04(self):
        """ Test grad_descent 04 """
        test_case, expected = self.generate_dataset(0.1)
        self.assertIn(test_case[e6.grad_descent(test_case)], expected)

if __name__ == '__main__':
    unittest.main()
