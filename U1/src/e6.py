"""
    @author: David E. Craciunescu
      @date: 2020/02/18 (yyyy/mm/dd)

    6. Program a function to determine if a number received as a parameter is
    perfect. Analyze the efficiency and complexity of the provided solution.

    A perfect number is a positive integer such that it is equal to the sum of
    its divisors. As with all problems, there are many ways to implement this.
"""
import math

def is_perfect_naive(num):
    """
        Calculates if a number is perfect in a naive way. This function iterates
        all the way up to the number and checks every element.

        With this approach, we would obtain:
        - Temporal Complexity => O(n)
        - Spacial Complexity => O(1)
    """
    return num == sum([current for current in range(1, num) if num % current == 0])

def is_perfect_optimized(num):
    """
        Calculates if a number is perfect in a non-naive way. This function
        takes into account:
        - Divisors present themselves in pairs when calculating.
        - With this approach one only need go up to sqrt(num).
        - Can store partial sum instead of occupying memory with list of
          divisors.

        With this approach we would obtain:
        - Temporal Complexity => O(√n)
        - Spacial Complexity => O(1)
    """
    sum_divisors = 0

    for current in range(1, int(math.sqrt(num))+1):
        # Is divisor of the number.
        if num % current == 0:
            sum_divisors += current

            # Different quotient is also a solution.
            if num / current != current:
                sum_divisors += (num // current)

    return num*2 == sum_divisors
