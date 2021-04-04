"""
    @author: David E. Craciunescu
      @date: 2020/02/25 (yyyy/mm/dd)

    2. We are tasked with storing n files on a magnetic tape (sequential path
    storage medium) in such a way that the average loading time for each of the
    files is minimized. In the magnetic tape, each time data is requested, the
    system will search the tape sequentially and then rewind back to the
    beginning after finishing the operation.

    Assume that along with the files, we are provided with their lengths and
    the amount of times the file has been searched for in the past. Assume the
    reading speed and the information density within the tape are constant.

    Design a greedy algorithm that minimizes the average loading time when
    searching for data in the magnetic tape. Analyze the efficiency and
    complexity for the provided solution.
"""
from typing import List


def store_files(files: List[int]) -> List[int]:
    """
        Sorts elements according to their weighted usage.

        @params:
            files: 2D array with length and access for file.

        The best way to store the files is according to the relation between
        the times they're accessed and their length. The tape will be stored
        optimally if we follow an ascending order defined by length/access_time.

        We're merely performing a sorting operation. According to the official
        Python documentation, the sort in Python is O(n log n) both on average
        and the worst case.
    """
    return sorted(files, key=lambda elem: elem[0] / elem[1])
