"""
Advent of Code 2021, day 6
Will Karnasiewicz
"""
from collections import Counter
from typing import List

# Part 1
def sim_laternfish(fish_states: List[int], days: int) -> int:
    fish_state_counts = Counter(fish_states)
    for day in range(days):
        temp_counter = Counter()
        for num, value in fish_state_counts.items():
            if num == 0:
                temp_counter[6] += value
                temp_counter[8] += value
            else:
                temp_counter[num - 1] += value
        fish_state_counts = temp_counter
    return fish_state_counts.total()

def test_day6_pt1():
    assert sim_laternfish([3,4,3,1,2], 18) == 26
    assert sim_laternfish([3,4,3,1,2], 80) == 5934

def test_day6_pt2():
    assert sim_laternfish([3,4,3,1,2], 256) == 26984457539

# Test Pt 1 and 2
test_day6_pt1()
test_day6_pt2()



if __name__ == "__main__":
    with open("./inputs/will-input.txt") as f:
        data = f.read()

    input_list = [int(i) for i in data.split(',')]

    print(f"Day 6 Part 1: {sim_laternfish(input_list, 80)}")
    print(f"Day 6 Part 2: {sim_laternfish(input_list, 256)}")
