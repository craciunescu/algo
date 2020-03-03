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
def store_files(files):
    """
        Sorts elements according to their weighted usage.

        @params:
            files: 2D array with length and access for file.
    """
    return sorted(files, key=lambda elem: elem[0])
