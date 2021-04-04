"""
    @author: David E. Craciunescu
      @date: 2020/03/03 (yyyy/mm/dd)

    6. Shrek, Donkey and Dragona have just arrived to the base of Lord
    Farquaad's towering castle determined to free Fiona from her confinement. As
    they suspected, the drawbridge is guarded by multiple soldiers. Worry not,
    for they suspected such a thing could happen and carried with them a huge
    amount of ladders of all kinds and lengths so that they could get over the
    wall easily.

    Unfortunately, no ladder would be enough for them to get over the wall.
    Dragona is also unable to fly that high, so they seemed to be stuck at
    first. But just when they were about to give up, Shrek realized that the
    ladders they brought with them were all made of iron, which could be easily
    welded by Dragona's fire.

    She can weld any two ladders with her fire breath, but the time it takes for
    them to be completely welded is equal to the sum of their length. For
    example, welding a 6-meter ladder and an 8-meter one would take 6+8 = 14
    units of time. If this ladder were then welded to a 7-meter ladder, the time
    it would take to weld them would be 14+7 = 21 units of time. With this
    approach, it would have taken 14+21 = 35 units of time to complete the
    ladder.

    Design an efficient algorithm that finds the best cost and way to weld the
    stairs so that Shrek takes as little time as possible to get past the wall.
    Indicate the data structures that were used to solve this exercise and
    justify their use. Assume the set of ladders they have always contains only
    the exact amount of ladders needed to get past the wall.

    Analyze the efficiency and complexity of the provided solution.

    ---

    Just like the previous two exercises. Once you discover what a priority
    queue can do, there are few things that can not benefit from it. In this
    case the provided vector is heapified in order to sort it and then the
    smallest two values are always added together (keeping count of the time
    elapsed while welding) and then added back to the heap.

    We obtain a very elegant complexity of O(nlogn), given that we have to
    iterate over all the elements once (O(n)) and add the sum of the smallest
    ones back to the heap, which is O(logn).
"""
import heapq as heap
from typing import List

def minimum_sum(vector: List[int]) -> int:
    """
        Adds the smallest two elements of the set together until adding them
        all.
    """
    time = 0

    # Check for input.
    if vector:
        heap.heapify(vector)

        # Add two smallest elements repeatedly.
        while vector:
            weld = heap.heappop(vector) + heap.heappop(vector)
            if vector:
                heap.heappush(vector, weld)

            time += weld

    return time
