import time
from typing import List


# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
# element appears at most twice. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be
# placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first
# k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
# extra memory.

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

def solution(data: List[int], allowed_duplicates: int) -> List:
    prev_nr = {"nr": data[0], "freq": 1, "remove": 0}
    cursor = 1
    while cursor < len(data) and data[cursor] != "_":
        if should_remove(prev_nr, data[cursor], allowed_duplicates):
            prev_nr["remove"] += 1
            prev_nr["freq"] += 1
        else:
            if data[cursor] != prev_nr["nr"]:
                if prev_nr["freq"] > allowed_duplicates:
                    cursor = remove_element_from_list(cursor, prev_nr, data)
                    prev_nr["remove"] = 0
                prev_nr["nr"] = data[cursor]
                prev_nr["freq"] = 1

            else:
                prev_nr["freq"] += 1
        cursor += 1
    return data


def remove_element_from_list(cursor, prev_nr, data: List):
    start = cursor - prev_nr['remove']
    step = start + prev_nr['remove']
    while start <= len(data) - 1 and (start + prev_nr['remove']) <= len(data) - 1:
        data[start] = data[step]
        start += 1
        step = start + prev_nr['remove']
    if step > len(data) - 1:
        for index in range(start, len(data)):
            data[index] = "_"
    return cursor - prev_nr['remove']


def should_remove(prev_nr, current_element, allowed_duplicates: int) -> bool:
    if prev_nr['nr'] == current_element and prev_nr["freq"] >= allowed_duplicates:
        return True
    return False


if __name__ == '__main__':
    start_time = time.time()
    list_data = [
        [1, 2, 3, 4, 5, 6],
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9]
    ]
    for x in list_data:
        print("{} solution is: {}".format(x, solution([i for i in x], 2)))

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
