#!/usr/bin/env python

"""
Advent of Code 2020, day 1
Will Karnasiewicz
"""

# Part 1

with open('./inputs/will-input.txt') as f:
    input_list = [int(line.rstrip('\n')) for line in f]

def expense_report_two_to_total(expense_txt, total):

    sorted_report = sorted(expense_txt)
    for expense in sorted_report:
        val_needed = total - expense
        if val_needed in sorted_report:
            return expense * val_needed

# Part 2

def expense_report_three_to_total(expense_txt, total):

    sorted_report = sorted(expense_txt)
    for expense in sorted_report:
        val_needed = total - expense
        try:
            subtotal = expense_report_two_to_total(expense_txt, val_needed)
            return expense * subtotal
        except:
            continue

if __name__ == "__main__":
    print(expense_report_two_to_total(input_list, 2020))
    print()
    print(expense_report_three_to_total(input_list, 2020))

