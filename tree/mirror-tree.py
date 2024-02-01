# Mirror a tree
import time


class Node:
    def __init__(self, name: str, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def solution(original_tree: Node):
    mirror_tree = Node(original_tree.name)
    if original_tree.left is not None:
        mirror_tree.right = solution(original_tree.left)
    if original_tree.right is not None:
        mirror_tree.left = solution(original_tree.right)
    return mirror_tree


def printTree(node: Node, branch: str = ""):
    print("Node {} = {}: ".format(branch, node.name))
    if node.left is not None:
        printTree(node.left, "left")
    if node.right is not None:
        printTree(node.right, "right")


if __name__ == '__main__':
    start_time = time.time()
    tree = Node("A",
                left=Node("B",
                          left=Node("D"),
                          right=Node("E")),
                right=Node("C",
                           left=Node("F"),
                           right=Node("G")))

    print("Original Tree")
    printTree(tree, "Root")

    mirror = solution(tree)
    print("solution is: ")
    printTree(mirror, "Root")

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
