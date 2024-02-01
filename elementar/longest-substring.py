import time
from typing import List


def solution(text: str) -> int:
    last_variant = []
    max_found = []
    for char in text:
        if isAdded(char, last_variant):
            dpl_index = getIndexOfDuplicated(char, last_variant)
            substr = getSubStringFromDuplicateIndex(dpl_index, last_variant)
            if len(substr) >= 0:
                last_variant = substr
                last_variant.append(char)
        else:
            last_variant.append(char)
            if len(max_found) < len(last_variant):
                max_found = last_variant
    print("max_found", max_found)
    return len(max_found)


def getCurrentChar(text, index) -> str:
    return text.index(index)


def getSubStringFromDuplicateIndex(index, variant: List):
    temp = []
    for i in range(len(variant)):
        if i > index:
            temp.append(variant[i])
    return temp


def getIndexOfDuplicated(char, variant: List) -> int:
    return variant.index(char)


def isAdded(char, variant: List) -> bool:
    return char in variant


if __name__ == '__main__':
    # abcabcabcddabab --> "abc"
    # rwwkerw --> "wker"
    start_time = time.time()
    print("solution is: {}".format(solution("pwwkew")))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
