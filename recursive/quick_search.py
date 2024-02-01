import math
import time
from typing import List


# "Quick Search", "Quick Sort", "Merge Sort" follow the same principle.
# "Quick Sort" - require an insert of element into the list --> sort(left, element) or sort(right, element)
# "Merge Sort" - require a merge of merge(sort(left, element), sort(right, element))
def solution(data: List[int], element: int):
    return search(data, element, 0)


def search(branch: List[int], element: int, count_steps: int) -> int:
    middle = math.floor(len(branch) / 2)
    if len(branch) == 0:
        return -1
    if element == branch[middle]:
        return count_steps

    print("{} == {}".format(element, branch[middle]))
    count_steps += 1

    # This algorithm is very similar when we want to traverse a binary tree.
    # Splitting the list in half we created the Leafs and nodes.
    right = branch[len(branch) - middle:]
    if element > branch[middle]:
        return search(right, element, count_steps)
    left = branch[:middle]
    if element < branch[middle]:
        return search(left, element, count_steps)


if __name__ == '__main__':
    start_time = time.time()
    # Must be ordered
    print("{}".format(solution([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 16], 10)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
