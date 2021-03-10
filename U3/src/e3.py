"""
    @author: David E. Craciunescu
      @date: 2021/02/22 (yyyy/mm/dd)

    3. Consider a function f(x) which:
    - Is known to have a unique local minimum called x0
        - At a point in the interval [p1, p2]
        - That CAN be p1 or p2.
    - Is strictly decreasing between [p1, x0]
    - Is strictly increasing between [x0, p2]

    Your task is to search, as efficiently as possible, for all points between
    p1 and p2 and find that unique local minimum. Formally, if f(x) = k, search
    for x ∈ [p1, p2].

    To simplify the process, instead of the exact value of each x, a range of
    values [α, β] can be indicated, with a β - α < ε, where x is found.

    The algorithm data will be the interval [p1, p2], the value k that is being
    searched for, and the value ε for the approximation.

"""

# Isn't this just the Indiana Croft exercise written formally?