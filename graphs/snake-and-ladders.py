
import time

import numpy as np


# https://leetcode.com/problems/snakes-and-ladders/description/?envType=study-plan-v2&envId=top-interview-150
def solution(this_matrix: np.ndarray) -> int:
    row = size - 1
    col = 0
    current_position_index = (row, col)
    moves = 0
    visited_positions = []
    while not visited(current_position_index, visited_positions):
        visited_positions.append((current_position_index[0], current_position_index[1]))
        nr = int(this_matrix[current_position_index[0]][current_position_index[1]])
        if matrix_nr[current_position_index[0]][current_position_index[1]] == pow(size, 2):
            moves += 1
            return moves
        if nr == -1:
            direction = 0
            if current_position_index[1] < matrix_nr[current_position_index[0]].size - 1:
                if (matrix_nr[current_position_index[0]][current_position_index[1] + 1] >
                        matrix_nr[current_position_index[0]][current_position_index[1]]):
                    direction = 1
                elif current_position_index[1] > 0:
                    direction = -1
            if direction == 0:
                return moves
            # going to the next column: backward/forward
            current_position_index = (current_position_index[0], current_position_index[1] + (1 * direction))
        else:
            print("found: {}".format(nr))
            moves += 1
            current_position_index = get_position(nr, matrix_nr)

    return moves


def visited(current: tuple, visited_positions) -> bool:
    for position in range(len(visited_positions)):
        item = visited_positions[position]
        if item[0] == current[0] and item[1] == current[1]:
            return True
    return False


def get_position(nr: int, this_matrix: np.ndarray) -> tuple:
    return np.where(this_matrix == nr)[0][0], np.where(this_matrix == nr)[1][0]


def init_matrix(this_matrix: np.ndarray, default_value: int = 0) -> np.ndarray:
    rows = size - 1
    start = size
    operation = 1
    while rows >= 0:
        for col in reversed(range(0, size)):
            if default_value != 0:
                this_matrix[rows][col] = default_value
            else:
                this_matrix[rows][col] = start
            start = abs((start * operation) - 1)
        start = this_matrix[rows][0] + size
        operation *= -1
        rows -= 1
    return this_matrix


if __name__ == '__main__':
    start_time = time.time()
    size = 6  # 2 <= size <= 20

    matrix_nr = init_matrix(np.zeros((size, size)))
    matrix = init_matrix(np.zeros((size, size)), -1)

    # ladder a link to another cell from upper level row
    # snake a link to another cell from same level row.
    # TODO: a ladder can take you to a lower layer too so we need to skip that as a bad solution
    # TODO: a snake move can be in a bad position we need to get only the best solution.
    # need to use the algorithm with buble search --> visited node and shortest path...
    matrix[3][1] = 35
    matrix[3][4] = 13
    matrix[5][1] = 15

    print(matrix_nr)
    print(matrix)

    print("total moves including the last position N^2: {}".format(solution(matrix)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
