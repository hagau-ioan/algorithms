import math
import time
from typing import List, Optional


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7] Output: 49 Explanation: The above vertical lines are represented by array [1,8,
# 6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

def solution(elements: List[int]) -> int:
    max_found = -math.inf
    current = 0
    while current < len(elements):
        found = find_max(current, elements)
        if found > max_found:
            max_found = found
        current += 1
    if max_found < 0:
        return 0
    return max_found


def find_max(start_index: int, elements: List[int]) -> int:
    max_found = -math.inf
    for i in range(start_index + 1, len(elements)):
        steps = i - start_index
        value = min(elements[i], elements[start_index])
        max_found = value * steps
    return max_found


if __name__ == '__main__':
    start_time = time.time()
    list_data = [
        [1, 2, 3, 4, 5, 6],
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9],
        [1, 4, 2, 3],
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [1, 2, 1],
        [1, 2, 4, 3]
    ]
    for x in list_data:
        print("{} solution is: {}".format(x, solution(x)))

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
