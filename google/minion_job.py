from typing import List


def solutions_ok(data: List, n: int) -> List:
    frequency = {}

    # Count the frequency of each number
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1

    # Remove numbers occurring more than n times
    return [num for num in data if frequency[num] <= n]


def solutions(data: List, n: int) -> List:
    filtered_list: List = []
    for worker_id in data:
        if check_worker_frequency(data, filtered_list, worker_id, n) is False:
            filtered_list.append(worker_id)
    return filtered_list


def check_worker_frequency(workers: List, filter_list: List, worker_id: int, freq: int) -> bool:
    if freq == 0:
        return True
    count = 0
    for i in workers:
        if i == worker_id:
            count += 1
        if count > freq:
            return True
    return False


if __name__ == '__main__':
    print(solutions([100, 100, 1, 0, 2, 4, 3, 3, 12, 4, 5, 5, 9, 100, 100, 1, 0, 2, 4, 3, 3, 12, 4, 5, 5, 9], 0))
    print(solutions_ok([100, 100, 1, 0, 2, 4, 3, 3, 12, 4, 5, 5, 9, 100, 100, 1, 0, 2, 4, 3, 3, 12, 4, 5, 5, 9], 0))
