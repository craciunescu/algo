"""
    @author: David E. Craciunescu
      @date: 2020/04/29 (yyyy/mm/dd)

    4. We'd like to program a robot to match cork stoppers to glass bottles at
    a recyling factory.

    The factory has N bottles and has one (and only one) cork stopper to match
    each bottle. The process would seem simple but there are a number of details
    we need to take into consideration first:
    - The bottles are all different from one another, just like the corks. Each
      bottle can only be closed with its correspondent cork and each cork only
      serves for a specific bottle.
    - The robot only know how to close bottles. It has the sensors needed to
      know if a cork is too big or too small for a bottle but is not programmed
      to compare corks or bottles between themselves. So the robot would not be
      able to compare between corks or bottles and sort them by thickness.
    - The robot has the space available and mechanical arms to place bottles and
      corks at will, for example in different positions of a table, if needed.

    Design an algorithm that follows the Divide and Conquer scheme to plug N
    bottles optimally. Analyze the complexity of the provided solution and explain
    the reasoning behind it.

    ---

    I think it is obvious that the complexity of this solution is O(nlogn). I
    used this as an opportunity to implement quicksort. We cannot compare
    elements between themselves so forcing us to use elements from the other
    list to order the first one was a pretty clever approach.
"""


def search_linear(val, data):
    """ Performs linear search and returns the index of val in data if found """

    for idx, elem in enumerate(data):
        if elem == val:
            return idx
    return None


def search_binary(val, data):
    """ Performs binary search and returns the index of val in data if found """

    def search_binary_aux(val, data, start, end):
        """ search_binary helper method """

        mid_idx = (start + end) // 2
        mid_val = data[mid_idx]

        # Basic cases.
        if mid_val == val:
            return mid_idx
        if mid_idx == end:
            return None

        # Not-so-basic cases.
        if mid_val < val:
            found = search_binary_aux(val, data, mid_idx+1, end)
        else:
            found = search_binary_aux(val, data, start, mid_idx)

        return found

    return search_binary_aux(val, data, 0, len(data)-1)

def pivot(val, data, start, end):
    """
        Standard QuickSort pivoting. Does not create auxiliary data structures.

        @params:
              val: the pivot value
             data: the data
            start: the start of the range in which to pivot
              end: the end of the range in which to pivot

        @returns: a tuple with:
             data: after pivoting the elements
             left: last index of left pointer in data
            right: last index of right pointer in data
    """
    left = start
    right = end

    # Iterate until unordered element
    while left < right:
        while data[left] < val:
            left += 1
        while data[right] > val:
            right -= 1

        # Swap if out of place
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    return (data, left, right)

def quick_sorted(data, compare, start, end):
    """
        Performs quicksort using pivots from a provided list instead of own.
        This implementation is optimized for a comparing list that is sorted.

        @params:
               data: the data to sort
            compare: from which to obtain pivots
              start: the start point of the sorting algorithm
                end: the end point of the sorting algorithm

        @returns: the sorted data
    """
    if start == end:
        return data

    # Obtain a pivot and sort sides.
    pivot_idx = search_binary(data[start], compare)
    pivot_elem = compare[pivot_idx]
    data, left, right = pivot(pivot_elem, data, start, end)

    # If not yet fully sorted.
    if start < right:
        quick_sorted(data, compare, start, right)
    if end > left:
        quick_sorted(data, compare, left, end)

    return data

def quick_unsorted(data, compare, start, end):
    """
        Performs quicksort using pivots from a provided list instead of own.

        @params:
            data: the data to sort
         compare: from where to obtain pivots
           start: the start point of the sorting algorithm
             end: the end point of the sorting algorithm

        @returns: the sorted data
    """
    if start == end:
        return data

    # Obtain a pivot and sort sides.
    pivot_idx = search_linear(data[start], compare)
    pivot_elem = compare[pivot_idx]
    data, left, right = pivot(pivot_elem, data, start, end)

    # If not yet fully sorted.
    if start < right:
        quick_unsorted(data, compare, start, right)
    if end > left:
        quick_unsorted(data, compare, left, end)

    return data

def match(set1, set2):
    """
        Returns the sorted match of two unordered iterables. Sorts the iterables
        by comparing with each other and not the set itself.

        @params:
            set1: the first data set
            set2: the second data set

        @returns:
            an ordered list of tuples with the elements found in both
    """
    set1 = quick_unsorted(set1, set2, 0, len(set1)-1)
    set2 = quick_sorted(set2, set1, 0, len(set2)-1)

    return list(zip(set1, set2))

