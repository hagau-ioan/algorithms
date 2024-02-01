import time
from typing import List

import numpy as np
from numpy import ndarray


def solution(_countries_colors: List[str], _neighbors: ndarray, current_country_index: int = 0):
    prev_neighbor_index = -1
    for neighbor_index in range(len(_neighbors[current_country_index])):
        # Compare the current country color with neighbor
        if current_country_index != neighbor_index and _neighbors[current_country_index][neighbor_index] != 0:
            if _countries_colors[current_country_index] == _countries_colors[neighbor_index]:
                # change the neighbor color
                _countries_colors[neighbor_index] = get_color_except(_countries_colors[neighbor_index])
                # Compare the prev neighbor color of current country with neighbor color
                if prev_neighbor_index != -1 and \
                        _countries_colors[neighbor_index] == _countries_colors[prev_neighbor_index]:
                    # change the neighbor color
                    _countries_colors[neighbor_index] = get_color_except(_countries_colors[neighbor_index])
            prev_neighbor_index = neighbor_index


# Get the next available color form the colors list. Reaching the end will search for a color from index 0
def get_color_except(_color: str) -> str:
    global colors
    for color_index in range(len(colors)):
        if colors[color_index] == _color:
            if color_index + 1 < len(colors):
                return colors[color_index + 1]
            else:
                return colors[0]
    return _color


# https://info.mcip.ro/?cap=Greedy&prob=816
if __name__ == '__main__':
    # Exceptions:
    # 1. Cannot exist a number of colors less than 3
    # 2. For countries count > 4 we should use a nr. of colors bigger than 3. --> 4

    nr_of_countries = 6
    start_time = time.time()
    colors = ["A", "V", "G", "R"]

    neighbors = np.zeros((nr_of_countries, nr_of_countries))

    # Set up the neighbors
    neighbors[0][1] = 1
    neighbors[0][2] = 1
    neighbors[0][3] = 1
    neighbors[0][4] = 1
    neighbors[0][5] = 1
    neighbors[1][2] = 1
    neighbors[1][4] = 1
    neighbors[1][5] = 1
    neighbors[2][3] = 1
    neighbors[2][4] = 1
    neighbors[3][4] = 1
    neighbors[4][5] = 1

    countries_colors = []
    for i in range(nr_of_countries):
        countries_colors.append(colors[0])  # add a default color to all countries

    for index in range(len(countries_colors)):
        solution(countries_colors, neighbors, index)

    for index in range(len(countries_colors)):  # run the algorithm for each country updating [countries_colors]
        print("Country {} has color {}".format(index + 1, countries_colors[index]))

    # print("{}".format(solution(countries_colors, neighbors)))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
