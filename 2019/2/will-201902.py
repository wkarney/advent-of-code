#!/usr/bin/env python

"""
Advent of Code 2019, day 2
Will Karnasiewicz
"""


def calc_intcode(input_list, noun, verb):
    """Function for transforming int_code

    Parameters
    ----------
    int_list : list
        The Intcode program (list of integers) to be transformed
    noun : int
        The value placed in address 1 prior to running program
    verb : int
        The value placed in address 2 prior to running program

    Returns
    -------
    list
        The original list of Intcode transformed per the program's rules
    """
    int_list = input_list[:]
    int_list[1] = noun
    int_list[2] = verb
    opcode_loc = 0
    while opcode_loc < len(int_list):
        if int_list[opcode_loc] == 1:
            int_list[int_list[opcode_loc + 3]] = (
                int_list[int_list[opcode_loc + 1]] + int_list[int_list[opcode_loc + 2]]
            )
            opcode_loc += 4
        elif int_list[opcode_loc] == 2:
            int_list[int_list[opcode_loc + 3]] = (
                int_list[int_list[opcode_loc + 1]] * int_list[int_list[opcode_loc + 2]]
            )
            opcode_loc += 4
        elif int_list[opcode_loc] == 99:
            break
        else:
            print(
                "There's an error with the Opcode. It needs to be 1, 2, \
                or 99."
            )
    return int_list[0]


# Part 1:
# Read in input file
with open("./inputs/will-input.txt") as file:
    for line in file:
        input_list = [int(num) for num in line.split(",")]

# Perform calculations and display answer
print(f"Part 1: {calc_intcode(input_list=input_list, noun=12, verb=2)}")

# Part 2
def intcode_zero_inverse(int_list, target):
    for noun in range(0, 100):
        for verb in range(0, 100):
            test_list = int_list
            if calc_intcode(test_list, noun=noun, verb=verb) == target:
                return noun, verb


noun, verb = intcode_zero_inverse(input_list, 19690720)
print(f"Part 2: {100*noun + verb}")
