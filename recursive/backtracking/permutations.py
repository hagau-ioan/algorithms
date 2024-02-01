import time
from typing import List


def solution(numbers, cursor):
    global counter_var
    if cursor == len(numbers) - 1:
        counter_var += 1
        print("counter={}, variant = {}".format(counter_var, numbers))
    else:
        for i in range(cursor, len(numbers)):
            numbers[cursor], numbers[i] = numbers[i], numbers[cursor]
            solution(numbers, cursor + 1)
            numbers[cursor], numbers[i] = numbers[i], numbers[cursor]  # backtrack


# Not so performant because we have 2 for cycle loop.
# The idea is simple: add the cursor number before/after a group,
# add the cursor number between elements of the group.
def solution_sec(numbers, cursor) -> List:
    if cursor == len(numbers) - 1:
        return [[numbers[cursor]]]
    else:
        queue = []
        queue_res: List
        queue_res = solution_sec(numbers, cursor + 1)
        nr = numbers[cursor]
        for variant in queue_res:
            queue.append([e for e in variant])  # 4,2,5
            queue[len(queue) - 1].insert(0, nr)  # 6,4,2,5
            queue.append([e for e in variant])
            queue[len(queue) - 1].append(nr)  # 4,2,5,6
            for i in range(len(variant) - 1):
                sub_queue = []
                for index, elem in enumerate(variant):
                    sub_queue.append(elem)
                    if i == index:
                        sub_queue.append(nr)
                queue.append(sub_queue)  # 4,6,2,5 | 4,2,6,5
    return queue


if __name__ == '__main__':
    counter_var = 0
    data = ["a", "b", "c", "d", "e"]
    start_time = time.time()
    print("variants first version: ")
    solution(data, 0)
    sol_sec = solution_sec(data, 0)
    print("\n\nvariants sec version: \n{}, \nnr. of permutations: {}".format(sol_sec, len(sol_sec)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
