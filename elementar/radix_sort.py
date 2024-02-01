import time
from typing import List


def solution(items: List) -> List:
    iterations = len(str(find_longest_element_length(items)))
    for iteration in reversed(range(iterations)):
        items = sort_data(items, iteration, iterations)
    return items


def sort_data(items: List, iteration: int, iterations: int) -> List:
    digit_list: List = get_digits(items, iteration, iterations)
    digit_list = sort_digits(digit_list)
    return update_items(digit_list)


def update_items(digits: List):
    items = []
    for item in digits:
        items.append(item['item'])
    return items


def get_digits(items: List, iteration: int, iterations: int) -> List:
    digits = []
    for item in items:
        # Preparation work to have a uniform data list from ['1', '10', '300'] to ['001', '010', '300']
        element = str(item)
        length = len(element)
        if length < iterations:
            element = str(element).zfill(iterations)
        digit = element[iteration]
        digits.append({"digit": int(digit), "item": item})
    return digits


def sort_digits(digits: List) -> List:
    # digits = sorted(digits, key=lambda x: x['digit']) # optimised from python env.
    # digits = sort_digits_unoptimised(digits)
    digits = sort_digits_by_counting(digits)
    return digits


# Another version of sorting, very unpopular, dummy, etc .... Use a merge sort for example
def sort_digits_unoptimised(digits: List) -> List:
    max_index = 0
    for i in range(len(digits) * len(digits)):
        if (max_index + 1) < len(digits) and digits[max_index]['digit'] > digits[max_index + 1]['digit']:
            digits.insert(max_index, digits.pop(max_index + 1))
            max_index += 1
        else:
            if max_index >= len(digits):
                max_index = 0
            else:
                max_index += 1
    return digits


# https://www.geeksforgeeks.org/counting-sort/
def sort_digits_by_counting(digits: List) -> List:
    # Creating an empty frequency list
    freq_list = [0 for i in range(max(digits, key=lambda x: x['digit'])['digit'] + 1)]
    # Creating an empty output list from "digits"
    output_list = [0 for i in range(len(digits))]

    # Each value digit will correspond to the index position of freq_list
    # Increment a counter for each pair(index(freq_list), value(digits)) found

    #  STEP 1
    for digit in digits:
        freq_list[digit['digit']] += 1

    #  STEP 2
    # SUM(n-1, n) into freq_list
    for index in range(len(freq_list) - 1):
        freq_list[index + 1] = freq_list[index] + freq_list[index + 1]

    #  STEP 3
    # Take the "digits" list and we iterate in reverse order
    for digit in reversed(digits):
        # Update the output list with value from freq_list[...index...]
        output_list[freq_list[digit['digit']] - 1] = digit
        # decrease the counter from freq_list because we handled the value already once.
        freq_list[digit['digit']] -= 1

    return output_list


def find_longest_element_length(numbers: List) -> int:
    # a built-in max search of the longest number.
    # can be used any max algorithm here
    return max(numbers)


if __name__ == '__main__':
    start_time = time.time()
    # sort_digits_by_counting([{'digit': 6, 'item': 346}, {'digit': 4, 'item': 234}, {'digit': 6, 'item': 56},
    #                          {'digit': 2, 'item': 2}, {'digit': 4, 'item': 34}, {'digit': 3, 'item': 123},
    #                          {'digit': 8, 'item': 345678}, {'digit': 2, 'item': 32}, {'digit': 1, 'item': 1},
    #                          {'digit': 0, 'item': 0}])
    data = [346, 234, 56, 2, 34, 123, 345678, 32, 1, 0]
    print("solution for {} is: {}".format(data, solution(data)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
