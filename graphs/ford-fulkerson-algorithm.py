# https://www.programiz.com/dsa/ford-fulkerson-algorithm
import math
import time


class Edge:

    def __init__(self, start: int, end: int, capacity: float) -> None:
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0


class EdgeGraph:
    residual: Edge
    edge: Edge

    def __init__(self, start: int, end: int, capacity: float):
        self.edge = Edge(start=start, end=end, capacity=capacity)

    def isResidual(self) -> bool:
        return self.edge.capacity == 0

    def remainingCapacity(self) -> float:
        return self.edge.capacity - self.edge.flow

    def augment(self, found_flow: float):
        # THIS IS THE KEY POINT
        self.edge.flow += found_flow
        self.residual.flow -= found_flow


class Algorithm:
    graph: [] = list
    visited: []
    max_flow: float = 0
    nr_of_nodes: int = 0

    def __init__(self, nr_of_nodes: int, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.graph = [list() for i in range(nr_of_nodes)]
        self.visited = [-1 for i in range(nr_of_nodes)]
        self.nr_of_nodes = nr_of_nodes

    def addEdge(self, start: int, end: int, capacity: int) -> None:
        if capacity <= 0:
            return
        edge_start = EdgeGraph(start, end, capacity)
        edge_end = EdgeGraph(end, start, 0)
        # assigning address. Changing the flow of one of the edge_start | edge_end
        # will trigger an augment(self, found_flow: float) change
        # THIS IS THE KEY POINT: start --> end --> start settings
        edge_start.residual = edge_end.edge  # to be able to go back and recalculate the flow values.
        edge_end.residual = edge_start.edge
        self.graph[start].append(edge_start)
        self.graph[end].append(edge_end)

    # Core algorithm flow
    def getMaxFlow(self):
        max_flow = 0
        self.visited = []
        found_flow = self.dfs(self.start, math.inf)
        while found_flow != 0:
            # self.visited_token += 1
            max_flow += found_flow
            self.visited = []
            found_flow = self.dfs(self.start, math.inf)
        return max_flow

    def dfs(self, node: int, flow: float) -> float:
        if node == self.end:
            return flow
        self.visited.append(node)
        children = self.graph[node]
        node_edge: EdgeGraph
        for node_edge in children:
            # (flow/capacity) --> capacity > flow and capacity - flow > 0
            remaining_capacity = node_edge.remainingCapacity()
            if remaining_capacity > 0 and (node_edge.edge.end not in self.visited):
                found_flow = self.dfs(node_edge.edge.end, min(flow, remaining_capacity))
                if found_flow > 0:
                    # will change the flow for node_edge (current node) but also for parent_node through reference
                    node_edge.augment(found_flow)
                    return found_flow
        return 0


def example_23_max_value() -> Algorithm:
    nr_of_nodes = 12
    s = nr_of_nodes - 2
    t = nr_of_nodes - 1

    alg = Algorithm(nr_of_nodes, s, t)

    # Edges from source
    alg.addEdge(s, 0, 10)
    alg.addEdge(s, 1, 5)
    alg.addEdge(s, 2, 10)

    # Middle edges
    alg.addEdge(0, 3, 10)
    alg.addEdge(1, 2, 10)
    alg.addEdge(2, 5, 15)
    alg.addEdge(3, 1, 2)
    alg.addEdge(3, 6, 15)
    alg.addEdge(4, 1, 15)
    alg.addEdge(4, 3, 3)
    alg.addEdge(5, 4, 4)
    alg.addEdge(5, 8, 10)
    alg.addEdge(6, 7, 10)
    alg.addEdge(7, 4, 10)
    alg.addEdge(7, 5, 7)

    # Edges to sink
    alg.addEdge(6, t, 15)
    alg.addEdge(8, t, 10)

    return alg


def example_20_max_value() -> Algorithm:
    nr_of_nodes = 6
    s = nr_of_nodes - 2
    t = nr_of_nodes - 1
    alg = Algorithm(nr_of_nodes, s, t)

    # Edges from source
    alg.addEdge(s, 0, 10)
    alg.addEdge(s, 1, 10)

    # Middle edges
    alg.addEdge(0, 2, 25)
    alg.addEdge(1, 3, 15)
    alg.addEdge(3, 0, 6)

    # Edges to sink
    alg.addEdge(3, t, 10)
    alg.addEdge(2, t, 10)

    return alg


def example_7_max_value() -> Algorithm:
    nr_of_nodes = 11
    s = nr_of_nodes - 2
    t = nr_of_nodes - 1
    alg = Algorithm(nr_of_nodes, s, t)

    # Edges from source
    alg.addEdge(s, 0, 7)
    alg.addEdge(s, 1, 2)
    alg.addEdge(s, 2, 1)

    # Middle edges
    alg.addEdge(0, 3, 2)
    alg.addEdge(0, 4, 4)
    alg.addEdge(1, 4, 5)
    alg.addEdge(1, 5, 6)
    alg.addEdge(2, 3, 4)
    alg.addEdge(2, 7, 8)
    alg.addEdge(3, 6, 7)
    alg.addEdge(3, 7, 1)
    alg.addEdge(4, 6, 3)
    alg.addEdge(4, 8, 3)
    alg.addEdge(4, 5, 8)
    alg.addEdge(5, 8, 3)

    # Edges to sink
    alg.addEdge(6, t, 1)
    alg.addEdge(7, t, 3)
    alg.addEdge(8, t, 4)

    return alg


if __name__ == '__main__':
    start_time = time.time()

    # n - The number of nodes in the graph including s and t.
    # s - The index of the source node, 0 <= s < n *
    # t - The index of the sink node, 0 <= t < n and t != s

    # working with a graph where the nodes got as id's --> numbers
    # s,t must have a symbolic id and will be a continue enumeration of nodes numbers: 6 - 2, 6 - 1
    # Instead of letter were used numbers because is much easier to work with.

    # Augmented Path: is a path of edges in the residual graph with unused capacity > 0 from s to t
    # https://www.youtube.com/watch?v=LdOnanfc5TM&ab_channel=WilliamFiset

    print("max flow: {}".format(example_23_max_value().getMaxFlow()))
    print("max flow: {}".format(example_20_max_value().getMaxFlow()))
    print("max flow: {}".format(example_7_max_value().getMaxFlow()))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
