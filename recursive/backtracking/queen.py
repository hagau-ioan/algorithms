import time

import numpy as np
from numpy import ndarray


def solution(size: int):
    matrix = np.zeros((size, size))  # create a matrix having size columns and size rows initialised with 0
    find(matrix, 0)
    # matrix[2][2] = 1
    # print_matrix(matrix)
    # valid = checkIsPositionValid(matrix, 4, 1)
    # if valid is False:
    #     print("Cannot position the element")
    # else:
    #     print("Position of the new element is valid.")


solution_count = 0


def find(matrix: ndarray, current_column: int):
    if current_column >= len(matrix):
        print_matrix(matrix)
        return
    for row in range(len(matrix)):
        if checkIsPositionValid(matrix, row, current_column):
            matrix[row][current_column] = 1
            find(matrix, current_column + 1)
            matrix[row][current_column] = 0


def checkIsPositionValid(matrix: ndarray, row_index: int, column_index: int) -> bool:
    # Check the column
    matrix_len = len(matrix)
    for i in range(matrix_len):
        if matrix[i][column_index] == 1 or matrix[row_index][i] == 1:
            return False

    for i in range(len(matrix - row_index)):
        check_one = row_index - i >= 0 and column_index - i >= 0
        check_two = row_index - i >= 0 and column_index + i < matrix_len
        check_three = row_index + i < matrix_len and column_index - i >= 0
        check_four = row_index + i < matrix_len and column_index + i < matrix_len
        diagonal_check = (check_one and matrix[row_index - i][column_index - i] == 1) \
                         or (check_two and matrix[row_index - i][column_index + i] == 1) \
                         or (check_three and matrix[row_index + i][column_index - i] == 1) \
                         or (check_four and matrix[row_index + i][column_index + i]) == 1

        if diagonal_check:
            return False
    return True


def print_matrix(matrix: ndarray):
    global solution_count
    print("{}.)\n {}".format(solution_count, matrix))
    solution_count += 1


if __name__ == '__main__':
    matrix_size = 4
    start_time = time.time()
    # 4 == 2; 5 == 10; 6 == 4; 7 = 40; 8 = 92 --> size == solutions
    print("{}".format(solution(matrix_size)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
