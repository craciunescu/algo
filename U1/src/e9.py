"""
    @author: David E. Craciunescu
      @date: 2020/02/18 (yyyy/mm/dd)

    9. Program a recursive function to calculate the following sum:
    S = 1 + 2 + 3 + 4 + (...) + n-1 + n.
    Analyze the efficiency and complexity of the provided solution.
"""
def summation(num):
    """ 
        Recursively calculates the sum of all the numbers between 1 and num.

        With this approach we get:
        - Time Complexity => O(n) [Basically doing a for loop recursively]
        - Space Complexity => O(n) [We have to store all the calls on the stack]
    """
    if num <= 1:
        return num
    return num + summation(num - 1)
