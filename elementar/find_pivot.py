import time
from typing import List, Any


# Pivot index solution:
# https://www.youtube.com/watch?v=FCWQZKmVrVU

def solution(numbers: List[int]):
    pivot_left_index = len(numbers)
    pivot_left = []

    for i in range(len(numbers)):
        if 0 < i < len(numbers):
            left = numbers[0:i]
            right = numbers[i + 1: len(numbers)]
            if len(left) > 0 and len(right) > 0:
                result = get_solution(left, right)
                if len(result) != 0:
                    if pivot_left_index > i and len(result) > 0:
                        pivot_left_index = i
                        pivot_left = result
                    print("A solution was found for index {} is [{},{},{}]".format(i, result[0], numbers[i], result[1]))
    if len(pivot_left) == 0:
        return -1
    return pivot_left_index, pivot_left


def get_solution(left_branch: List[int], right_branch: List[int]):
    start_left_index = len(left_branch) - 1
    start_right_index = 0
    if start_left_index == 0:
        return []

    left_result = []
    right_result = []

    left_sum = left_branch[start_left_index]
    right_sum = right_branch[start_right_index]
    left_result.append(left_branch[start_left_index])
    right_result.append(right_branch[start_right_index])
    while start_left_index >= 0 and start_right_index < len(right_branch):
        if left_sum > right_sum:
            start_right_index += 1
            if start_right_index < len(right_branch):
                right_sum += right_branch[start_right_index]
                right_result.append(right_branch[start_right_index])
        elif left_sum < right_sum:
            start_left_index -= 1
            if start_left_index >= 0:
                left_sum += left_branch[start_left_index]
                left_result.insert(0, left_branch[start_left_index])
        else:
            # What we will do if we have multiple solution for same index pivot
            return [left_result, right_result]
    return []


if __name__ == '__main__':
    start_time = time.time()

    input_data = [1, 7, 3, 6, 5, 6]
    # input_data = [1, 2, 3]
    # input_data = [50, 20, 10, 20, 3, 10, 70, 10, 5, 5]
    final = solution(input_data)
    print("{} : solution is: {}".format(input_data, final))

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
