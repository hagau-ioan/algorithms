import time
from typing import List

moves = 0


# (2 pow disk_nr) - 1 = nr. of solutions
def solution(n, x):
    return power(n, x)


def power(n, x) -> int:
    if x == 1:
        return n  # Stop condition
    if x == 0:
        return 1  # stop condition
    r = power(n, x - 1)
    return r * n  # solving the small problem


if __name__ == '__main__':
    start_time = time.time()
    print("{}".format(solution(3, 4)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
