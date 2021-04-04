"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    8. Program a recursive procedure to obtain the inverse number of a given
    one. Example: 627 -> 726. Analyze the efficiency and complexity of the
    provided solution.
"""
# Testing
import unittest
from U1.src.e8 import inverse

class TestInverseMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U1/src/e8.py """

    # Test inverse
    def test_inverse01(self):
        """ Test inverse """
        provided = inverse(1234)
        expected = 4321
        self.assertEqual(provided, expected)

    def test_inverse02(self):
        """ Test inverse """
        provided = inverse(1000)
        expected = 1
        self.assertEqual(provided, expected)

    def test_inverse03(self):
        """ Test inverse """
        provided = inverse(1)
        expected = 1
        self.assertEqual(provided, expected)

    def test_inverse04(self):
        """ Test inverse """
        provided = inverse(1230)
        expected = 321
        self.assertEqual(provided, expected)

if __name__ == '__main__':
    unittest.main()
