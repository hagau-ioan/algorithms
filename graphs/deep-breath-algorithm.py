import time


# choosing the current_node is very important because we will be able to have access only to the current_node
# and the edges of that current node.
# Example: This is useful when we want to know all deep connections of one person: friends of friends...
def solution(current_node: str, graph: dict):
    print("current node: {}".format(current_node))
    visited = [current_node]
    queue = [current_node]
    while len(queue) > 0:
        start_node = queue.pop()
        for node in graph[start_node]:
            if (node in visited) is False:
                visited.append(node)
                queue.append(node)
                print("checking edge node: {}".format(node))


if __name__ == '__main__':
    data = {
        '1': ['2', '5'],
        '2': ['1', '3', '6'],
        '3': ['2', '4', '7'],
        '4': ['3', '8'],
        '5': ['1', '9', '6'],
        '6': ['2', '5', '7', '10'],
        '7': ['3', '6', '11', '8'],
        '8': ['7', '12'],
        '9': ['5', '10'],
        '10': ['6', '9', '11'],
        '11': ['10', '7', '12'],
        '12': ['8', '11']
    }
    start_time = time.time()
    print("{}".format(solution('7', data)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
