"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    1. For an even-length non-empty array of non-repeating
    pseudo-randomly-generated positive integer values, form unique pairs between
    such values and return the pair that yields the highest result when both its
    numbers are added together.

    Design a voracious algorithm that creates pairs in such a way that the
    maximum value of the sums is the smallest biggest sum possible, showing that
    candidate selection function used provides an optimal solution.

    ---

    It seems that the optimal solution to this problem would consist of:
    1. Sorting the array -> O(nlog(n))
    2. Iterating the array both ways and making pairs from start and end.
    3. While iterating, storing the maximum found each iterations. O(1)
"""
def get_min_pair_sum(values):
    """ Returns the minimum possible maximum sum out of two values """

    pair_values = []
    maximum = []

    # Sort the values.
    values.sort()

    # Iterate over array.
    for i in range(int(len(values)/2)):
        start = values[i]
        end = values[len(values)-1-i]

        # New pair found.
        pair_values.append([start, end])

        # Check for max pair.
        new_max = start+end > sum(maximum)
        if new_max:
            maximum = [start, end]

    return sum(maximum)
