"""
    @author: David E. Craciunescu
      @date: 2020/04/30 (yyyy/mm/dd)

    6. After passing through the Tile Room and stealing the Craddle of Life,
    Indiana Croft faces a new challenge before leaving the Cursed Temple! The
    Temple itself is located on a bridge under which there is a deep darkness.

    Fortunately, this place also appears in the diary. The bridge crosses the
    so-called Valley of Shadows, which begins with a descent slope (not
    necessarily constant), so that after reaching the lowest point he must start
    to climb to the other end of the bridge.

    Just at the bottom of the valley, one can find a river, but the diary does
    not give any specific information about its whereabouts, so Indiana Croft
    only knows the river can be found "at the bottom of the valley" and nothing
    else. On the slopes, there are sharp rocks.

    If Indiana Croft had time, he could easily find the point where to get off
    the bridge to get exactly to the river, given that he has a laser pointer
    that he can measure heights with and tells him how many meters there are
    from the bridge to the ground at a certain point. Unfortunately, the priests
    of the Temple have already found him and they are chasing him down. If he
    doesn't jump off the bridge they'll catch him before he gets off the bridge.
    Our adventurer must quickly find the position of the river to get off and
    flee safely.

    In order to save our hero, design the algorithm that Indiana Croft should
    use to find the minimum point of the valley under the conditions mentioned
    above. The algorithm must be efficient, for he cannot afford to waste a
    single second: at least in the best case it must have a logarithmic order.

    You can consider the time that it takes for Indiana Croft to travel along
    the bridge as negligible and that the estimate of the point of the river
    where to drop off can have an approximation error of ε meters (ε is a given
    constant).

    Explain the reasoning behind the provided solution and analyze its
    efficiency and complexity.

    ---

    The problem basically forces us to use Gradient Descent. Since we have to
    optimize at each move and cannot afford to waste time on the absolute
    optimal of answers, we look at what happens to the slope of the function
    created by the heights of the bridge.

    Even though recursive, the complexity of this algorithm is clearly O(logn),
    since at each iteration, no matter what happens, the dataset is divided in
    half.

    I also took extra efford to make the implementation space efficient as well.
    This means that no extra storage elements or auxiliary temporal variables
    are used when calculating the gradient descent, only a dataset, a start
    point and an endpoint.

    Last thing. I ignored the "the estimate of the point of the river where to
    drop off can have an approximation error of ε meters" and chose to go
    directly with the lowest possible error there could be.
"""
def grad_descent(data):
    """ Simple algorithm for gradient descent """

    def grad_descent_aux(data, start, end):
        """ grad_descent auxiliary function """

        # Basic cases.
        length = end - start
        if length <= 2:
            return start if data[start] < data[end] else end

        # Not-so-basic cases.
        mid_idx = (start + end) // 2
        if data[mid_idx - 1] < data[mid_idx]:
            pos = grad_descent_aux(data, start, mid_idx)
        else:
            pos = grad_descent_aux(data, mid_idx, end)

        return pos

    return grad_descent_aux(data, 0, len(data)-1)
