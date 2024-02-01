# Fuel Injection Perfection
# =========================
#
# Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the
# LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a
# bit of sabotage while you're at it -- so you took the job gladly.
#
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP
# each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need
# to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.
#
# The fuel control mechanisms have three operations:
#
# 1) Add one fuel pellet 2) Remove one fuel pellet 3) Divide the entire group of fuel pellets by 2 (due to the
# destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow
# this to happen if there is an even number of pellets)
#
# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of
# operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number
# up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
#
# For example: solution(4) returns 2: 4 -> 2 -> 1 solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1 Quantum
# antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need
# to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure
# out the most efficient way to sort and shift the pellets down to a single pellet at a time.
#
# The fuel control mechanisms have three operations:
#
# 1) Add one fuel pellet 2) Remove one fuel pellet 3) Divide the entire group of fuel pellets by 2 (due to the
# destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow
# this to happen if there is an even number of pellets)
#
# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of
# operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number
# up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
#
# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Python cases --
# Input:
# solution.solution('15')
# Output:
#     5
#
# Input:
# solution.solution('4')
# Output:
#     2
#
# -- Java cases --
# Input:
# Solution.solution('4')
# Output:
#     2
#
# Input:
# Solution.solution('15')
# Output:
#     5

def remove_zeros_at_end(bin_nr):
    return bin(bin_nr).rstrip("0")


def len_of_zeros_from_end_of_bin(bin_nr):
    return len(bin(bin_nr)) - len(remove_zeros_at_end(bin_nr))  # len of zero's representing the number division to 2


def solutions(n):
    n = int(n)
    # Note: cannot use recursion because we will get a memory issue problem.
    # Exceptional cases
    if n <= 1:
        return 0  # Exception case 9
    if n == 3:
        return 2

    operations = 0
    while n > 1:
        if n == 3:
            operations += 2
            break
        zeros = len_of_zeros_from_end_of_bin(n)
        if zeros == 0:
            operations += 1
            if len_of_zeros_from_end_of_bin(n + 1) > len_of_zeros_from_end_of_bin(n - 1):
                n += 1
            else:
                n -= 1
        else:
            operations += zeros
            n = int(remove_zeros_at_end(int(n)), 2)

    return operations


if __name__ == '__main__':
    elements = [673, 1346, 64, 3000, 789, 15, 3, 23, 0, 1, 4, 234235435345345345353425435346]
    # elements = [16]
    for i in elements:
        print("For the number: {} found {} operations".format(i, solutions(i)))
