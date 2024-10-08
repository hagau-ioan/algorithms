from typing import List


# Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with
# doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar
# panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field,
# which wreaks havoc on the solar panels. You and your team of henchmen have been assigned to repair the solar
# panels, but you'd rather not take down all the panels at once if you can help it, since they do help power the
# space station and all!
#
# You need to figure out which sets of panels in any given array you can take offline to repair while still
# maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the
# maximum output of each array actually is. Write a function solution(xs) that takes a list of integers representing
# the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of
# those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5],
# then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product
# 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".
#
# Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output
# level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining
# energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to
# produce the positive output of the multiple of their power values). The final products may be very large,
# so give the solution as a string representation of the number.
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
# solution.solution([2, 0, 2, 2, 0])
# Output:
#     8
#
# Input:
# solution.solution([-2, -3, 4, -5])
# Output:
#     60
#
# -- Java cases --
# Input:
# Solution.solution({2, 0, 2, 2, 0})
# Output:
#     8
#
# Input:
# Solution.solution({-2, -3, 4, -5})
# Output:
#     60

def solutions(panels: List) -> str:
    positive_panels = [i for i in panels if i > 0]
    negative_panels = [i for i in panels if i < 0]

    if len(positive_panels) == 0 and len(panels) <= 1 and len(negative_panels) == 1:
        return negative_panels[0]  # [-2]
    elif len(positive_panels) == 0 and len(panels) > 1 and len(negative_panels) == 1:
        return "0"  # [-2, 0] | [0, -2]

    if len(negative_panels) % 2 != 0:
        negative_panels.pop(negative_panels.index(max(negative_panels)))

    final = positive_panels + negative_panels
    if len(final) > 0:
        x = 1
        for value in positive_panels + negative_panels:
            x *= value
        return str(x)

    return str(0)


if __name__ == '__main__':
    q = [0, -4, 0, -3]
    print("{}".format(solutions(q)))
    q = [2, 0, 2, 2, 0]
    print("{}".format(solutions(q)))
    q = [-2, -3, 4, -5]
    print("{}".format(solutions(q)))
    q = [0, -4]
    print("{}".format(solutions(q)))
    q = [-4]
    print("{}".format(solutions(q)))
    q = [0]
    print("{}".format(solutions(q)))
