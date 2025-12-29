import time
from typing import List


def solution(numbers: List, max_nr: int = -1, current_index: int = 0) -> int:
    if current_index > len(numbers) - 1:
        return max_nr
    found_max = max_nr
    if numbers[current_index] > found_max:
        found_max = numbers[current_index]
    return solution(numbers, found_max, current_index + 1)


if __name__ == '__main__':
    start_time = time.time()
    print("{}".format(solution([100, 7, 3, -1, 10, 6])))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
