"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    8. Program a recursive procedure to obtain the inverse number of a given
    one. Example: 627 -> 726. Analyze the efficiency and complexity of the
    provided solution.

    Note: I am yet to find a solution to this without using global variables.
    This works, I've checked the call stack myself.
"""
def inverse_aux(number: int, result:int = 0) -> int:
    """
        Recursively obtains the inverse number of the provided one

        With this approach, we obtain:
        - Time Complexity => O(n)
            [This is obvious, we must iterate all numbers once no matter what.]
        - Space Complexity => O(n)
            [You must store at least the number of iterations as calls on the
            stack.]
    """

    if number > 0:
        reminder = number % 10
        result = (result*10) + reminder
        inverse_aux(number // 10, result)

    return result

def inverse(number: int) -> int:
    """ Recursively obtains the inverse number of the provided one """
    return inverse_aux(number)
