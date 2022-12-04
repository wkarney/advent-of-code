"""
Advent of Code 2021, day 7
Will Karnasiewicz
"""
from math import ceil, floor
from statistics import median, mean
from typing import List, Tuple

# Part 1
def define_crab_formation(positions: List[int]) -> Tuple[int, int]:
    optimal_pos = int(median(positions))
    fuel_usage = 0
    for pos in positions:
        fuel_usage += abs(optimal_pos - pos)
    return optimal_pos, fuel_usage


def test_day7_pt1():
    assert define_crab_formation([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])[0] == 2
    assert define_crab_formation([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])[1] == 37


# Part 2
def define_crab_formation_2(positions: List[int]) -> Tuple[int, int]:
    med_pos = int(median(positions))
    mean_pos = int(round(mean(positions)))
    if mean_pos > med_pos:
        ub = mean_pos
        lb = med_pos
    else:
        ub = med_pos
        lb = mean_pos
    options = {}
    for i in range(lb, ub + 1):
        fuel_usage = 0
        for pos in positions:
            fuel_usage += sum(range(abs(i - pos) + 1))
        options[i] = fuel_usage
    min_fuel = min(options.values())
    return [key for key in options if options[key] == min_fuel][0], min_fuel


def define_crab_formation_2b(positions: List[int]) -> Tuple[int, int]:
    """Streamlined function that only looks around mean value"""
    mean_flr = int(floor(mean(positions)))
    mean_ceil = int(ceil(mean(positions)))
    options = {}
    for i in [mean_flr, mean_ceil]:
        fuel_usage = 0
        for pos in positions:
            fuel_usage += sum(range(abs(i - pos) + 1))
        options[i] = fuel_usage
    min_fuel = min(options.values())
    return [key for key in options if options[key] == min_fuel][0], min_fuel


def test_day7_pt2():
    assert define_crab_formation_2([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])[0] == 5
    assert define_crab_formation_2([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])[1] == 168


# Test Pt 1 and 2
test_day7_pt1()
test_day7_pt2()


if __name__ == "__main__":
    with open("./inputs/will-input.txt") as f:
        data = f.read()

    input_list = [int(i) for i in data.split(",")]

    print(f"Day 7 Part 1: Fuel consumed: {define_crab_formation(input_list)[1]}")
    print(f"Day 7 Part 2: Fuel consumed: {define_crab_formation_2b(input_list)[1]}")
