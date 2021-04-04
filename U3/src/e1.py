import math
from typing import List

def coincident(vector: List[int]) -> bool:
    """
        @author: David E. Craciunescu
          @date: 2020/04/26 (yyyy/mm/dd)

        1. For a non-empty vector of non-repeating pseudo-randomly-generated
        integer values ordered in increasing order, design a divide-and-conquer
        algorithm that finds if the vector is coincident.

        A coincident vector is that in which at least one value is contained in an
        index equal to that value. An example would be: [-14, -2, 2, 4, 7, 9].
        The value 2 can be found in index [2], therefore the vector is
        coincident.

        The complexity of the provided solution should not exceed O(logn).
        Consider as inputs the vector and its size.

        ---
        Obtains if a vector is coincident in O(√n) time.
    """
    length = len(vector)
    is_odd_length = length % 2 != 0
    if is_odd_length: length -= 1

    pos = math.ceil(length/2)
    iteration = 1

    while 0 <= pos < len(vector):
        if vector[pos] == pos: return True

        jump = math.ceil(length // 2^(iteration+1))

        if vector[pos] > pos: pos -= jump
        else: pos += jump

        iteration += 1

    return False
