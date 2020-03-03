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
def get_min_pair_sum(values):
    """
        Returns the minimum possible maximum sum out of two values

        It seems that the optimal solution to the problem would be:
        1. Sort the array => O(n log(n))
        2. Iterate over the array and make pairs from start and end => O(n)
        3. Store the biggest value found each iteration => O(1)
        4. Return stored value => O(1)

        With this approach, we would obtain:
        - Time Complexity => O(nlog(n))
        - Space Complexity => O(n)
    """

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
