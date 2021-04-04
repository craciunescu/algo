"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    1. For an even-length non-empty array of non-repeating
    pseudo-randomly-generated positive integer values, form unique pairs between
    such values and return the pair that yields the highest result when both its
    numbers are added together.

    Design a greedy algorithm that creates pairs in such a way that the
    maximum value of the sums is the smallest biggest sum possible, showing that
    candidate selection function used provides an optimal solution.
"""
from typing import List


def get_min_pair_sum(values: List[int]) -> int:
    """
        Returns the minimum possible maximum sum out of two values

        It seems that the optimal solution to the problem would be:
        1. Sort the array => O(n log(n))
        2. Iterate over half the array and make pairs from start and end => O(n/2) => O(n)
        3. Store the biggest value found each iteration => O(1)
        4. Return stored value => O(1)

        With this approach, we would obtain:
        - Time Complexity => O(nlog(n))
        - Space Complexity => O(n)
    """
    # Initialization and preprocessing
    current_max = []
    values.sort()

    size = len(values)
    midpoint = size // 2
    iterable_values = enumerate(values[:midpoint])

    # Iterate over array.
    for idx, val in iterable_values:

        start = val
        end = values[size-idx-1]
        new_pair = [start, end]

        # Check for max pair.
        new_max_found = sum(new_pair) > sum(current_max)
        if new_max_found:
            current_max = new_pair

    return sum(current_max)
    
