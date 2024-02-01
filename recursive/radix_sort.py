import time
from typing import List, Optional


# https://www.geeksforgeeks.org/radix-sort/
def solution(data: List[int]) -> Optional[List]:
    if len(data) == 0:
        return None
    return traverseTree(data)


def traverseTree(data: List[int]) -> Optional[List]:
    pass


if __name__ == '__main__':
    start_time = time.time()
    # In terms of Big O notation, the merge sort is referred to as: O(n log n)
    print("{}".format(solution([100, 90, 40, 30, 10, 5, 4, 3, 2, 1, 0, 300, 500])))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
