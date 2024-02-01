import time
from math import sqrt


# Se citesc două numere naturale a și b (a mai mic decât b) având cel mult 9 cifre fiecare. Afișați câte numere din
# intervalul [a,b] au exact 3 divizori. Exemplu: În intervalul [11,50] numerele care au exact 3 divizori sunt 25 și
# 49, deci se va afișa 2.

def solution(a, b) -> int:
    count = 0
    if a > b:
        return count
    for nr in range(a, b):
        if is_prime(nr) is True and has_a_single_dev(nr) is True:
            print(nr)
            count += 1
    return count


def is_prime(nr: int) -> bool:
    if nr == 2 or nr == 3:
        return True
    # Still need more logic here for prime numbers
    # the rules 1-41, 41 - 100 and > 1000
    # https://www.vedantu.com/maths/how-to-find-prime-numbers
    return True


def has_a_single_dev(nr: int) -> bool:
    if sqrt(nr) == int(sqrt(nr)):
        for n in range(2, int(sqrt(nr))):
            if int(nr % n) == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    start_time = time.time()
    print("solution is: {}".format(solution(11, 50)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
