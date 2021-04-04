"""
    @author: David E. Craciunescu
      @date: 2020/02/18 (yyyy/mm/dd)

    7. Write a program that receives a positive number N and obtains
    the amount of prime numbers and the amount of perfect numbers there are
    between 1 and N. Analyze the efficiency and complexity of the provided
    solution.

    For this we could reuse the already defined methods in e5 and e6, but that
    would yield a highly inefficient program. We could solve this problem in two
    different ways:
    - Implementing the Sieve of Erastothenes.
    - Tweaking the implementation of e5 and e6 in order to return amounts and
      not booleans.
"""
from typing import List, Tuple
from U1.src.e6 import is_perfect_optimized as is_perfect

def amount_primes(num: int) -> int:
    """
        Calculates the amount of perfect numbers between 1 and 'num'.

        With this approach, we obtain:
        - Temporal Complexity => O(n)
        - Spacial Complexity => O(n)
    """
    
    # Generate detected primes. 0 and 1 are not primes 
    primes = [True for _ in range(num+1)]
    primes[0] = primes[1] = False # Clearly not primes
    current = 2

    # Check for unmarked numbers
    while current**2 <= num:
        # If not marked => prime
        if primes[current]:
            # Mark all multiples as non-primes
            for multiple in range(current**2, num+1, current):
                primes[multiple] = False

        current += 1

    # Return amount of true values in list
    return len([prime for prime in primes if prime])

def amount_perfects(num: int) -> int:
    """
        Calculates the amount of prime numbers between 1 and 'num'.

        With this approach, we obtain:
        - Temporal Complexity => O(n√n)
        - Spacial Complexity => O(1)
    """
    counter = 0
    for num in range(1, num+1):
        if is_perfect(num):
            counter += 1

    return counter

def amount_primes_perfects(num: int) -> Tuple[int, int]:
    """
        Returns the amount of primes and perfect numbers between 1 and 'number'.
        Complexities stay the same as original implementations.
    """
    return (amount_primes(num), amount_perfects(num))
