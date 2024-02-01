import time

moves = 0


# (2 pow disk_nr) - 1 = nr. of solutions
def solution(disk_nr, tower_first, tower_sec, tower_third):
    global hanoi_towers, moves
    if disk_nr == 1:
        moves += 1
        print(f"Move disk 1 from {tower_first['name']} to {tower_third['name']}")
        if len(hanoi_towers[0]['values']) > 0:
            hanoi_towers[2]['values'].insert(0, hanoi_towers[0]['values'].pop())  # solving the small problem
        return  # Stop condition

    solution(disk_nr - 1, tower_first, tower_third, tower_sec)

    print(f"Move disk {disk_nr} from {tower_first['name']} to {tower_third['name']}")
    moves += 1
    if len(hanoi_towers[0]['values']) > 0:
        # solving the small problem
        hanoi_towers[2]['values'].insert(0, hanoi_towers[0]['values'].pop())
    solution(disk_nr - 1, tower_sec, tower_first, tower_third)


# solution_sec(first, third, sec)
def solution_sec(disc_nr, first, second, third):
    # A not working wel solution form internet: youtube
    if disc_nr == 1:
        print(f"Move disk = 1 from {first} to {second}")
        return
    solution_sec(disc_nr - 1, first, third, second)
    solution_sec(disc_nr - 1, third, second, first)


if __name__ == '__main__':
    hanoi_towers = [
        {"name": "A", "values": [3, 2, 1]},
        {"name": "B", "values": []},
        {"name": "C", "values": []}
    ]
    max_nr_of_disc = len(hanoi_towers[2]['values'])
    start_time = time.time()
    # solution_sec(len(hanoi_towers[0]['values']), "X", "Y", "Z")
    print("Start: T{}={}, T{}={}, T{}={}".format(
        hanoi_towers[0]['name'], hanoi_towers[0]['values'],
        hanoi_towers[1]['name'], hanoi_towers[1]['values'],
        hanoi_towers[2]['name'], hanoi_towers[2]['values']))
    solution(len(hanoi_towers[0]['values']), hanoi_towers[0], hanoi_towers[1], hanoi_towers[2])
    print("End: T{}={}, T{}={}, T{}={}, Nr. of moves: {}".format(
        hanoi_towers[0]['name'], hanoi_towers[0]['values'],
        hanoi_towers[1]['name'], hanoi_towers[1]['values'],
        hanoi_towers[2]['name'], hanoi_towers[2]['values'], moves))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
