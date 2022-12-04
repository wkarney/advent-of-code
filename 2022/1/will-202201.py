#!/usr/bin/env python

"""
Advent of Code 2022, day 1
Will Karnasiewicz
"""

# Input Data

with open('./inputs/will-input.txt') as f:
    elves = f.read().split('\n\n')
    strings = [item.split('\n') for item in elves]
    input_list = [list(map(int, item)) for item in strings]

# # Parts 1 and 2

def max_rations(inputs):
    max_cals = 0
    max_cals = sum(input_list[0])
    for elf in input_list[1:]:
        if sum(elf) >= max_cals:
            max_cals = sum(elf)
    return max_cals

def top_rations(inputs):
    max_cals = sorted([sum(elf) for elf in input_list[:3]])
    for elf in input_list[3:]:
        if sum(elf) >= max_cals[0]:
            max_cals[0] = sum(elf)
            max_cals = sorted(max_cals)
    return sum(max_cals)


if __name__ == "__main__":
    print(f"Part 1: {max_rations(input_list)}")
    print(f"Part 2: {top_rations(input_list)}")
