"""
    @author: David E. Craciunescu
      @date: 2020/02/26 (yyyy/mm/dd)

    3. For a non-emtpy vector of length n, find the minimum and maximum element
    of the vector. The type of data the vector contains is not relevant to the
    problem, but performing comparisons between elements in the vector is an
    extremely expensive operation, so you should minimize the amount of
    comparisons.

    Implement a greedy method that makes a maximum of (3/2)n comparisons.
    Analyze the efficiency and complexity for the provided solution.
"""
from typing import List


def min_and_max(vector: List[int]):
    """
        Returns minimum and maximum elements in a vector while realizing the
        minimum amount of comparisons between elements.

        By using the Tournament Method, we compare the elements in pairs through
        to the next stage, this can only leave one element at the end.

        With this method we obtain a max of comparisons that follow the formula:
        if n is odd => 3(n-1)/2
        if n is even => 3(n/2)-2
        Both are bounded by (3/2)n comparisons.

        The complexity of the solution is clearly O(n).
    """
    if not vector: return []

    length = len(vector)
    pair = [vector[0], vector[1]]
    even_len = length % 2 == 0

    # Make sure we start in the right place
    if even_len:
        min_current, max_current = min(pair), max(pair)
        idx = 2
    else:
        min_current = max_current = vector[0]
        idx = 1

    # Iterate while looking for candidates
    while idx < length - 1:
        current_val, next_val = vector[idx], vector[idx+1]
        found_new_minimum = current_val < next_val

        if found_new_minimum:
            max_candidate, min_candidate = next_val, current_val
        else:
            max_candidate, min_candidate = current_val, next_val

        max_current = max(max_current, max_candidate)
        min_current = min(min_current, min_candidate)

        idx += 2

    return [max_current, min_current]
