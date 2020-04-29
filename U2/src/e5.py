"""
    @author: David E. Craciunescu
      @date: 2020/03/03 (yyyy/mm/dd)

    5. You are given a non-directed graph G = <N, A>, where N = {1, ..., n} is
    the set of nodes and A ⊆ NxN is the set of edges. Each edge (i,j) ∈ A has an
    associated cost Cij (Cij > ∀i, j ∈ N; if (i,j) ∉ A can be considered Cij =+ ∞).
    Let M be the cost matrix of the graph G, that is, M[i,j] = Cij (since the
    non-directed graph is that (i,j) = (j,i) so the matrix M is symmetric).

    Having as data (1) the number of nodes n, and (2) the cost matrix M, find
    the minimum path between nodes 1 and n, and the length of said path using
    the Dijkstra algorithm. When implementing the algorithm, take into
    consideration the following ideas:
    - Create or make use of a data structure that stores the known temporal
      distances for the vertices the algorithm hasn't traveled to yet.
    - Select as candidate the one with the least known temporal distance,
      eliminate it from the set of vertices not traveled to before, and update
      the rest of the temporal distances if they can be improved using the
      current vertex.
    - Store the way in which the graph was traversed from vertex 1 to vertex n
      (not necessarily equal to the set of decisions taken).

    Analyze the efficiency and complexity of the provided solution.

    ---

    Pretty much the same schema used for the previous exercise was used for this
    one, only here we're taking into consideration distances instead of looking
    for a spanning tree.

    The explanation is exactly the same one, and with the same data structure,
    we obtain a very similar complexity. In this case it is O(V + ElogV), as per
    theoretical specification, where V is the amount of vertices and E is the
    amount of edges.
"""
import heapq as heap
def path_shortest(graph, start):
    """ Pythonic minheap implementation of dijkstra's algorithm """

    # Initialize all distances to infinity but the start one.
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    paths = [(0, start)]

    # I legitimately believe this block of code is so clear it explains itself.
    # I'll eventually eliminate even this comment after correcting.
    while paths:
        current_distance, current_node = heap.heappop(paths)
        neighbors = graph[current_node].items()

        for neighbor, weight in neighbors:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heap.heappush(paths, (distance, neighbor))

    return distances
