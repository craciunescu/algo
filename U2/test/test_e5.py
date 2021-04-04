"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    5. You are given a non-directed graph G = <N, A>, where N = {1, ..., n} is
    the set of nodes and A ⊆ NxN is the set of edges. Each edge (i,j) ∈ A has an
    associated cost Cij (Cij > ∀i, j ∈ N; if (i,j) ∉ A can be considered Cij =+ ∞).
    Let M be the cost matrix of the graph G, that is, M[i,j] = Cij (since the
    non-directed graph is that (i,j) = (j,i) so the matrix M is symmetric).

    Having as data (1) the number of nodes n, and (2) the cost matrix M, find
    the minimum path between nodes 1 and n, and the length of said path using
    the Dijkstra algorithm

    Analyze the efficiency and complexity of the provided solution.
"""
# Testing
import unittest
from U2.src.e5 import path_shortest

class TestPathShortestMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e5.py """

    def test_path_shortest01(self):
        """ Test path_shortest """
        self.assertEqual(path_shortest(), )

    def test_path_shortest02(self):
        """ Test path_shortest """
        self.assertEqual(path_shortest(), )

    def test_path_shortest03(self):
        """ Test path_shortest """
        self.assertEqual(path_shortest(), )

    def test_path_shortest04(self):
        """ Test path_shortest """
        self.assertEqual(path_shortest(), )

if __name__ == '__main__':
    unittest.main()
