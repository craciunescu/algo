"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    8. Program a recursive procedure to obtain the inverse number of a given
    one. Example: 627 -> 726. Analyze the efficiency and complexity of the
    provided solution.
"""
def inverse_aux(number, result=0):
    """ Recursively obtains the inverse number of the provided one """

    if number > 0:
        reminder = number % 10
        result = (result*10) + reminder
        inverse_aux(number // 10, result)

    return result

def inverse(number):
    """ Recursively obtains the inverse number of the provided one """
    return inverse_aux(number)
