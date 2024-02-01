import time


# Find the shortest path from [current_node] to [destination_node]

# Example of the [all_paths] content

# [['4'], ['4', '8'], ['4', '7'], ['4', '3']]
# [['4'], ['4', '8'], ['4', '7'], ['4', '3'], ['4', '8', '12']]
# [['4'], ['4', '8'], ['4', '7'], ['4', '3'], ['4', '8', '12'], ['4', '7', '6'], ['4', '7', '11'], ['4', '7', '10']]
# [['4'], ['4', '8'], ['4', '7'], ['4', '3'], ['4', '8', '12'], ['4', '7', '6'], ['4', '7', '11'], ['4', '7', '10'], ['4', '3', '2']]
# [['4'], ['4', '8'], ['4', '7'], ['4', '3'], ['4', '8', '12'], ['4', '7', '6'], ['4', '7', '11'], ['4', '7', '10'], ['4', '3', '2']]
# [['4'], ['4', '8'], ['4', '7'], ['4', '3'], ['4', '8', '12'], ['4', '7', '6'], ['4', '7', '11'], ['4', '7', '10'], ['4', '3', '2'], ['4', '7', '6', '5']]
# [['4'], ['4', '8'], ['4', '7'], ['4', '3'], ['4', '8', '12'], ['4', '7', '6'], ['4', '7', '11'], ['4', '7', '10'], ['4', '3', '2'], ['4', '7', '6', '5']]
# Final: ['4', '7', '10']

def solution(graph: dict, current_node: str, destination_node: str) -> list:
    print("from={}, to={}".format(current_node, destination_node))
    # classic queue algorithm according to breath graph algorithm.
    queue = [current_node]
    # usually breath graph algorithm has a Visited list to skip the elements already visited
    # store all combination of nodes path
    all_paths = [[current_node]]
    # final result
    final_path = []
    # backup exit emergency solution from while cycle.
    # Also, because of this we will get [all_paths] variations one by one and we will check those
    count_all_found_paths = 0

    while count_all_found_paths < len(all_paths):
        # the algorithm [all_paths] suppose to go for each node assigned to parent-node one deep level by one deep
        # level. Ex: [2,1][2,3][2,4]
        # next depp level: [2,1,5][2,3,7][2,4,8]
        # next depp level: [2,1,5,9][2,3,7,10][2,4,8,12]
        # [2,3,7,10] - is success
        variation_path = all_paths[count_all_found_paths]
        current_node = variation_path[-1]  # getting the last element from the [variation_path]

        if destination_node in graph[current_node]:
            variation_path.append(destination_node)
            final_path = variation_path
            break

        for node in graph[current_node]:
            if node not in queue:  # skip the nodes already in queue
                new_path = variation_path[:]  # init new path with current segment of working path from [all_paths]
                new_path.append(node)
                all_paths.append(new_path)  # continue to extend the [all_path] with more other combination of paths.
                queue.append(node)

        # print(all_paths)

        count_all_found_paths += 1

    return final_path


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while 1:
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node

        if node2 in next_nodes:
            current_path.append(node2)
            return current_path

        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)

                # To avoid recursive
                previous_nodes.add(next_node)  # Queue
        # Continue to next path in list
        path_index += 1
    # No path is found


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
    start_time = time.time()
    print("{}".format(solution(data, '2', '10')))
    print("{}".format(shortest_path(data, '2', '10')))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
