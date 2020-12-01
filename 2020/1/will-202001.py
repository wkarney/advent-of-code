#!/usr/bin/env python

"""
Advent of Code 2020, day 1
Will Karnasiewicz
"""

import itertools
import math

# Input Data

with open('./inputs/will-input.txt') as f:
    input_list = [int(line.rstrip('\n')) for line in f]

# Parts 1 and 2

def expense_report_pairs(expense_txt, total, quantity):
    for group in list(itertools.combinations(expense_txt, quantity)):
        if sum(group) == total:
            return math.prod(group)
    raise Exception("No solution found!")


if __name__ == "__main__":
    print(f"Part 1: {expense_report_pairs(input_list, 2020, 2)}")
    print(f"Part 2: {expense_report_pairs(input_list, 2020, 3)}")
