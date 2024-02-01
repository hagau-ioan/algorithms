import math
import time
from typing import List, Optional


# "Quick Search", "Quick Sort", "Merge Sort" follow the same principle.
# "Quick Sort" - require an insert of element into the list --> sort(left, element) or sort(right, element)
# "Merge Sort" - require a merge of sort(merge(left, right))
def solution(data: List[int]) -> Optional[List]:
    if len(data) == 0:
        return None
    return traverseTree(data)


def traverseTree(branch: List[int]) -> Optional[List]:
    if len(branch) == 1:
        return branch
    #  Split the list in half
    middle_index = math.floor(len(branch) / 2)
    left = branch[:middle_index]
    right = branch[middle_index:]

    # goto the deepest possible value when list size == 1
    data = traverseTree(left) + traverseTree(right)
    return sort(data)  # return the sub list sorted.


# TODO: can use radix sorting algorithm
def sort(data) -> List:
    # O(n^2) - sorting. Linear Sort
    for j in range(len(data)):  # the sorted sublist LEFT + RIGHT need to be sorted: linear sort
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp
    return data


if __name__ == '__main__':
    start_time = time.time()
    # In terms of Big O notation, the merge sort is referred to as: O(n log n)
    print("{}".format(solution([100, 90, 40, 30, 10, 5, 4, 3, 2, 1, 0, 300, 500])))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
