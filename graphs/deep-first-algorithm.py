import time


# choosing the current_node is very important because we will be able to have access only to the current_node
# and the edges of that current node.
# Example: This is useful when we want to know all deep connections of one person: friends of friends...
def solution(current_node: str, graph: dict):
    print("current node: {}".format(current_node))
    for node in graph[current_node]:
        print("checking edge node: {}".format(node))
        solution(node, graph)


if __name__ == '__main__':
    data = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    start_time = time.time()
    print("{}".format(solution('a', data)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
