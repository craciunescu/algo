"""
    @author: David E. Craciunescu
      @date: 2020/02/19 (yyyy/mm/dd)

    4. You are given a non-directed graph G = <N, A>, where N = {1, ..., n} is
    the set of nodes and A ⊆ NxN is the set of edges. Each edge (i,j) ∈ A has an
    associated cost Cij (Cij > ∀i, j ∈ N; if (i,j) ∉ A can be considered Cij =+ ∞).
    Let M be the cost matrix of the graph G, that is, M[i,j] = Cij (since the
    non-directed graph is that (i,j) = (j,i) so the matrix M is symmetric).

    Having as data (1) the number of nodes n, and (2) the cost matrix M, find
    the minimum support tree of a graph G using Prim's algorithm.
"""
# Testing
import unittest
from src import e4

class TestMinPrimMethods(unittest.TestCase):
    """ Test methods in craciunescu@github.com/algo/U2/src/e4.py """

    def test_prim01(self):
        """ Test prim """

        # Picture of graph provided here https://shorturl.at/rELP4
        provide = {
            'A': {'B': 0.5, 'C': 3, 'E': 0},
            'B': {'A': 0.5, 'E': 0.7},
            'C': {'A': 3, 'D': -4.1, 'E': 2},
            'D': {'C': -4.1, 'F': 11},
            'E': {'A': 0, 'B': 0.7, 'C': 2, 'D': 1, 'F': 7, 'G': -1},
            'F': {'D': 11, 'E': 7, 'J': 3},
            'G': {'E': -1, 'H': 4, 'I': -1, 'J': 0.2},
            'H': {'H': 4},
            'I': {'G': -1, 'J': -2},
            'J': {'F': 3, 'G': 0.2, 'I': -2}
        }

        expect = {
            'A': {'B', 'E'},
            'E': {'D', 'G'},
            'G': {'H', 'I'},
            'I': {'J'},
            'D': {'C'},
            'J': {'F'}
        }

        self.assertEqual(dict(e4.prim(provide, 'A')), expect)

    def test_prim02(self):
        """ Test prim """

        # Linear graph and non-connected node.
        provide = {
            'A': {'B': 1},
            'B': {'A': 1, 'C': 1},
            'C': {'B': 1, 'D': 1},
            'D': {'C': 1, 'E': 1},
            'E': {'D': 1},
            'F': {}
        }

        expect = {
            'D': {'E', 'C'},
            'C': {'B'},
            'B': {'A'}
        }

        self.assertEqual(dict(e4.prim(provide, 'D')), expect)

    def test_prim03(self):
        """ Test prim """

        # Empty graph.
        provide = {}
        expect = {}

        self.assertEqual(dict(e4.prim(provide, 'B')), expect)

if __name__ == '__main__':
    unittest.main()
