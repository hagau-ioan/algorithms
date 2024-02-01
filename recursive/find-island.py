import time
from typing import List

import numpy as np

# we have a territory with water, land and islands. We need to identify the position of islands.
# if some territories will touch the edge of the continent those cannot be considered islands.
# We have a matrix of size (x,x). Cells are filled by default with 0(water). Some cells are filled with 1(land)
# If some of these lands will touch the edge of continent those cannot be considered islands.


final_edges = []


# Construct two lists:
# 1. edges
# 2. candidate islands
# findEdgesAndPaths --> will construct these two lists
def findEdgesAndIslands(data: np.ndarray) -> List:
    global final_edges
    row_index = 0
    col_index = 0
    edges = []
    island_variant = []
    final_paths = []
    while 0 <= row_index < len(data) and 0 <= col_index < len(data[row_index]):
        if isLand(data, row_index, col_index):  # is land
            if col_index == 0:
                edges.append([row_index, col_index])  # Add the first island from matrix as an edge land
            else:
                if isDuplicatedEntry(island_variant, row_index, col_index) is False:
                    island_variant.append([row_index, col_index])  # there is more land and is not at edge
                if (isLand(data, row_index, col_index + 1)
                        and isDuplicatedEntry(island_variant, row_index, col_index + 1) is False):
                    # there is more land on the right side from current
                    island_variant.append([row_index, col_index + 1])
                if (isLand(data, row_index, col_index - 1)
                        and isDuplicatedEntry(island_variant, row_index, col_index - 1) is False):
                    # there is more land on the left side from current
                    island_variant.append([row_index, col_index - 1])
                if (isLand(data, row_index + 1, col_index)
                        and isDuplicatedEntry(island_variant, row_index + 1, col_index) is False):
                    # there is more land on up above current
                    island_variant.append([row_index + 1, col_index])
                if (isLand(data, row_index - 1, col_index)
                        and isDuplicatedEntry(island_variant, row_index - 1, col_index) is False):
                    # there is more land on bottom under current
                    island_variant.append([row_index - 1, col_index])
        else:
            if len(island_variant) > 0:
                final_paths.append(island_variant)
            island_variant = []
        col_index += 1
        if col_index >= len(data[row_index]):
            if len(island_variant) > 0:
                if isDuplicatedEntry(edges, row_index, col_index - 1) is False:
                    edges.append([row_index, col_index - 1])  # Add the last island from matrix as an edge land
                    final_paths.append(island_variant)
            island_variant = []
            row_index += 1
            col_index = 0

    final_edges = edges
    return final_paths


# Remove some duplicated from candidate islands.
# TODO: This can be optimised, so we do not need this anymore.
def isDuplicatedEntry(path: List, x, y) -> bool:
    if len(path) == 0:
        return False
    for item in path:
        if item[0] == x and item[1] == y:
            return True
    return False


def isLand(data: np.ndarray, row_index, column_index) -> bool:
    return 0 <= row_index < len(data) and 0 <= column_index < len(data[row_index]) \
        and data[row_index][column_index] == 1


# Recursive solution to search for all islands which are not connected to an edge: the candidate islands
# Final cleanup
def solution(edge_element, data, index) -> bool:
    if index >= len(data):
        return False
    if isDuplicatedEntry(data[index], edge_element[0], edge_element[1]):
        result = data.pop(index)
        for x in result:
            solution(x, data, 0)
    else:
        solution(edge_element, data, index + 1)
    return False


if __name__ == '__main__':
    start_time = time.time()
    size = 6

    matrix = np.zeros((size, size))

    # matrix[0][0] = 1
    # matrix[1][1] = 1
    # matrix[1][3] = 1
    # matrix[1][4] = 1
    # matrix[1][5] = 1
    # matrix[2][2] = 1
    # matrix[2][4] = 1
    # matrix[3][0] = 1
    # matrix[3][2] = 1
    # matrix[3][4] = 1
    # matrix[4][0] = 1
    # matrix[4][2] = 1
    # matrix[4][3] = 1
    # matrix[5][0] = 1
    # matrix[5][2] = 1
    # matrix[5][5] = 1

    matrix[0][0] = 1
    matrix[1][1] = 1
    matrix[1][3] = 1
    matrix[1][4] = 1
    matrix[1][5] = 1
    matrix[2][2] = 1
    matrix[2][4] = 1
    matrix[3][0] = 1
    matrix[3][1] = 1
    matrix[3][4] = 1
    matrix[4][0] = 1
    matrix[4][2] = 1
    matrix[4][3] = 1
    matrix[5][0] = 1
    matrix[5][5] = 1

    print("initial matrix: \n", matrix)
    final_paths_data = findEdgesAndIslands(matrix)
    print("edges:", final_edges)
    for e in final_edges:
        solution(e, final_paths_data, 0)

    matrix_2 = np.empty((size, size), str)
    for e in final_paths_data:
        for i in e:
            matrix_2[i[0]][i[1]] = "1"

    print("final matrix: \n", matrix_2)

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
