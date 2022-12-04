"""
Advent of Code 2021, day 2
Will Karnasiewicz
"""
from typing import List

# Part 1
def find_sub_path_product(path_list) -> int:
    coords = [0, 0]
    for command, magnitude in path_list:
        if command == "forward":
            coords[0] += int(magnitude)
        elif command == "up":
            coords[1] -= int(magnitude)
        else:
            coords[1] += int(magnitude)
    return coords[0] * coords[1]


# Testing examples provided
EX_DATA = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

ex_data_list = [x.split(" ") for x in EX_DATA.split("\n")]


def test_day2_pt1():
    assert find_sub_path_product(ex_data_list) == 150


# Test Pt 1
test_day2_pt1()

# Part 2
def find_revised_sub_path(path_list) -> int:
    aim = 0
    coords = [0, 0]
    for command, magnitude in path_list:
        if command == "forward":
            coords[0] += int(magnitude)
            coords[1] += aim * int(magnitude)
        elif command == "up":
            aim -= int(magnitude)
        else:
            aim += int(magnitude)
    return coords[0] * coords[1]


def test_day2_pt2():
    assert find_revised_sub_path(ex_data_list) == 900


# Test Pt 2
test_day2_pt2()

if __name__ == "__main__":
    with open("./inputs/will-input.txt") as f:
        input_list = [line.split(" ") for line in f]

    print(f"Day 2 Part 1: {find_sub_path_product(input_list)}")
    print(f"Day 2 Part 2: {find_revised_sub_path(input_list)}")
