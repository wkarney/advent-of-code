"""
Advent of Code 2021, day 1
Will Karnasiewicz
"""
from typing import List


def depth_inc_counter(depth_list: List[int], sum_size: int) -> int:
    total = 0
    for count, value in enumerate(depth_list):
        if count > sum_size - 1 and sum(
            depth_list[count - (sum_size - 1) : count + 1]
        ) > sum(depth_list[count - 1 - (sum_size - 1) : count]):
            total += 1
    return total


# Testing examples provided
EX_DATA = """199
200
208
210
200
207
240
269
260
263"""

ex_data_list = [int(x) for x in EX_DATA.split("\n")]
assert depth_inc_counter(ex_data_list, 1) == 7
assert depth_inc_counter(ex_data_list, 3) == 5

if __name__ == "__main__":
    with open("./inputs/will-input.txt") as f:
        input_list = [int(line.rstrip("\n")) for line in f]

    print(f"Day 1 Part 1: {depth_inc_counter(input_list, 1)}")
    print(f"Day 1 Part 2: {depth_inc_counter(input_list, 3)}")
