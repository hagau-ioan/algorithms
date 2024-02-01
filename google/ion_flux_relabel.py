from typing import List


# Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label
# them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with the order
# of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:
#
#    7
#  3   6
# 1 2 4 5
#
# Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of
# positive integers representing different flux converters - which returns a list of integers p where each element in
# p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such
# converter.  For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4,
# and 7 in a perfect binary tree of height 3, which is [3, 6, -1].
#
# The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root,
# h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree
# with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p
# contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.
#
# Languages
# =========
#
# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
#
# -- Python cases --
# Input:
# solution.solution(3, [7, 3, 5, 1])
# Output:
#     -1,7,6,3
#
# Input:
# solution.solution(5, [19, 14, 28])
# Output:
#     21,15,29

def solutions(levels, search_elements) -> List:
    root_node_element = (2 ** levels) - 1
    found_parents = []

    for elem in search_elements:
        if elem > root_node_element:
            return []

    for elem in search_elements:
        found_parents.append(find_element(root_node_element, elem, levels))
    return found_parents


def find_element(parent_element, search_element, nr_of_levels):
    if nr_of_levels < 0:
        return -2

    if search_element == parent_element:
        return -1  # first case success found

    nr_of_total_nodes_on_last_level = (2 ** (nr_of_levels - 1))
    left_node_element = parent_element - nr_of_total_nodes_on_last_level
    right_node_element = parent_element - 1

    if search_element == left_node_element or search_element == right_node_element:
        return parent_element  # second case success found

    found_element = ""
    if search_element > left_node_element:
        found_element = find_element(right_node_element, search_element, nr_of_levels - 1)
    elif search_element < left_node_element:
        found_element = find_element(left_node_element, search_element, nr_of_levels - 1)
    return found_element


if __name__ == '__main__':
    h = 3
    q = [4, 7, 5]
    print("{}".format(solutions(h, q)))
