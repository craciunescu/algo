"""
    @author: David E. Craciunescu
      @date: 2020/03/03 (yyyy/mm/dd)

    4. You are given a non-directed graph G = <N, A>, where N = {1, ..., n} is
    the set of nodes and A ⊆ NxN is the set of edges. Each edge (i,j) ∈ A has an
    associated cost Cij (Cij > ∀i, j ∈ N; if (i,j) ∉ A can be considered Cij =+ ∞).
    Let M be the cost matrix of the graph G, that is, M[i,j] = Cij (since the
    non-directed graph is that (i,j) = (j,i) so the matrix M is symmetric).

    Having as data (1) the number of nodes n, and (2) the cost matrix M, find
    the minimum support tree of a graph G using Prim's algorithm. For your
    implementation, consider the following ideas:
    - Unlike Kruskal's algorithm (which creates the tree using independent
      connected components that are joined together, Prim's algorithm is based
      on the idea of building an increasingly large, starting with a single node
      and ending by coating the entire graph.
    - The algorithm begins with a tree of a node, to which a second node is
      added, then a third node, etc., until the n nodes are joined together. The
      way to choose a node is looking for the nearest node to the whole tree,
      without creating cycles.
    - As the size of the tree grows, the search for the nearest node becomes
      complicated. For the algorithm to be efficient, take into consideration
      the following guidelines:
      - Create a data structure to store the best distance from each node to the
        set of nodes of the tree.
      - Do not exceed a time complexity of O(n²).
    - Storing how the tree was created is necessary, for example, by indicating
      to which node of the tree the new candidate is being joined.

    Analyze the efficiency and complexity of the provided solution.

    ----
    The data structure that was used for this implemenetation was a priority
    queue (through the use of a MinHeap). Thanks to the standard python
    implementation.

    With this, we can standarize the format of an edge (weight, start, end) in a
    tuple, and the heap itself will take care to always give us back the edge
    that is the closest in constant time.

    The time complexity of the provided solution is, as per the theoretical
    definition of Prim's Algorithm, O((V+E) log V), where V is the number of
    vertices and E is the number of edges. This happens because each vertex is
    inserted in the priority queue only once, and the insertion in a prio queue
    takes logarithmic time.
"""
from collections import defaultdict
import heapq as heap
from typing import Dict
from numbers import Number

def prim(graph: Dict[chr, Number], start: chr) -> Dict[chr, Number]:
    """ Pythonic minheap implementation of prim's algorithm """

    # Check empty input.
    if not graph:
        return {}

    # Initialize path in tree and visited nodes.
    min_span_tree = defaultdict(set)
    visited = set([start])

    # Get all edges from start point.
    # << Python implement minheap by default >>
    neighbors = graph[start].items()
    edges = [(weight, start, end) for end, weight in neighbors]
    heap.heapify(edges)

    while edges:
        weight, start, end = heap.heappop(edges)

        # Check for cycles.
        if end not in visited:
            visited.add(end)
            min_span_tree[start].add(end)

            # Add edges of the newly visited node.
            neighbors = graph[end].items()
            for next_node, weight in neighbors:
                # Check for cycles.
                if next_node not in visited:
                    heap.heappush(edges, (weight, end, next_node))

    return min_span_tree
