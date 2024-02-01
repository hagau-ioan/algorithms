# A palindrome is a word, number, or a phrase that reads the same forwards as well as backward, for instance “kayak”,
# “1001”, “Was it a car or a cat I saw?”, or “ABBA”.
#
# I love palindromes — read more on why they are fun on this Wikipedia page. Did you know that the longest palindrome
# was 58,795 letters long?
import math
import time


def solutionSimple(text: str) -> bool:
    text = text.replace(" ", "").lower()

    diff = math.inf
    index_start = 0
    index_end = len(text) - 1
    while diff >= 1:
        if text[index_start] != text[index_end]:
            return False
        diff = index_end - index_start
        index_end -= 1
        index_start += 1
    return True


# Found all palindromes substrings from a text
def solutionWithSubstring(text: str) -> str:
    text = text.replace(" ", "").lower()
    main_index = 0
    float_index = main_index + 2
    max_substr_length = -math.inf
    max_substr = ""
    while main_index < len(text) and float_index < len(text):
        temp = text[main_index:float_index]
        temp_rev = temp[::-1]
        if temp == temp_rev:
            print("found: ", temp)
            if len(temp) >= max_substr_length:
                max_substr_length = len(temp)
                max_substr = temp
        float_index += 1
        if float_index >= len(text):
            main_index += 1
            float_index = main_index + 2
    return max_substr


if __name__ == '__main__':
    start_time = time.time()

    print("solution is -> palindromes simple: {}."
          .format(solutionSimple("Was it a car or a cat I saw")))
    # Was it a car 1001 or a cat I saw
    sol = solutionWithSubstring("abracadabra")
    print("solution is -> palindromes with substring: {} with size {}."
          .format(sol, len(sol)))

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
