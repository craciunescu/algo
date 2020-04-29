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
def min_and_max(vector):
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
    if not vector:
        return []

    length = len(vector)
    pair = [vector[0], vector[1]]
    even_len = length % 2 == 0

    if even_len:
        minimum, maximum = min(pair), max(pair)
        idx = 2
    else:
        minimum = maximum = vector[0]
        idx = 1

    while idx < length - 1:
        new_min = vector[idx] < vector[idx+1]

        if new_min:
            maximum = max(maximum, vector[idx+1])
            minimum = min(minimum, vector[idx])
        else:
            maximum = max(maximum, vector[idx])
            minimum = min(minimum, vector[idx+1])

        idx += 2

    return [maximum, minimum]
