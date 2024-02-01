import time


# choosing the current_node is very important because we will be able to have access only to the current_node
# and the edges of that current node.
# Example: This is useful when we want to know all deep connections of one person: friends of friends...
# A MUCH SIMPLER SOLUTION
def solution(graph: dict, start_node: str, dest_node: str):
    queue = [[int(start_node), 0, start_node]]
    visited = []
    while len(queue) > 0:
        node = queue.pop()
        current_node, path_graph_length, path_graph = node
        visited.append(current_node)
        # do the work for shortest path
        if current_node == dest_node:
            return node
        for neighbour in graph[str(current_node)]:
            if neighbour not in visited:
                queue.append([neighbour, path_graph_length + 1,
                              "{}, {}".format(path_graph, neighbour)])
    return []


if __name__ == '__main__':
    data = {
        '1': ['2', '5'],
        '2': ['1', '3'],
        '3': ['2', '4', '7'],
        '4': ['8', '7', '3'],
        '5': ['1', '9', '6'],
        '6': ['2', '5', '7', '10'],
        '7': ['3', '6', '11', '8', '10'],
        '8': ['4', '7', '12'],
        '9': ['5', '10'],
        '10': ['6', '9', '11'],
        '11': ['10', '7', '12'],
        '12': ['8', '11']
    }
    start = '2'
    destination = '10'
    start_time = time.time()
    result = solution(data, start, destination)
    last_node, path_length, path = result
    print("start path is = {} and destination is = {} --> path length[nr.edges]={}, path={}"
          .format(start, destination, path_length, path))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
