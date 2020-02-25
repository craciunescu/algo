"""
    @author: David E. Craciunescu
      @date: 2020/02/17 (yyyy/mm/dd)

    5. Program a funciton to determine if a number received as a parameter is
    prime. Analyze the efficiency and complexity of the provided solution(s).

    A prime number is a number greater than 1 that cannot be formed by
    multiplying two smaller natural numbers. As with all problems, there are
    many ways to implement this.
"""
import math

def is_prime_naive(number):
    """
        Calculates if a number is prime in a naive way. This function iterates
        all the way up to 'number' and checks every element.

        With this approach, we would obtain:
        - Temporal Complexity => O(n)
        - Spacial Complexity => O(1)
    """
    is_prime = True

    if number <= 1:
        is_prime = False
    else:
        current = 2
        while is_prime and current < number:
            is_prime = (number % current != 0)
            current += 1

    return is_prime

def is_prime_optimized(number):
    """
        Calculates if a number is prime in a non-naive way. This function takes
        into account:
        - Even numbers cannot be primes. Counter increment by 2.
        - If 2 divides a number, then the number divided by two divides n as
          well.

        With this approach, we would obtain:
        - Temporal Complexity => O(√n)
        - Spacial Complexity => O(1)
    """
    is_prime = True

    if number <= 1:
        is_prime = False
    else:
        current = 3
        while is_prime and current <= math.sqrt(number):
            is_prime = (number % current != 0)
            current += 2

    return is_prime
