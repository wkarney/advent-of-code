"""
Advent of Code 2021, day 3
Will Karnasiewicz
"""
from typing import List

# Part 1
def get_gamma(diag_list: List[str]) -> str:
    diag_size = len(diag_list[0]), len(diag_list)
    binary_counts = [0] * len(diag_list[0])
    for diag in diag_list:
        for pos, val in enumerate(diag):
            if val == "1":
                binary_counts[pos] += 1
    gamma = [str(-int(x) // (diag_size[1] // -2)) for x in binary_counts]
    return "".join(gamma)


def gam_to_ep_calc(gamma: str) -> str:
    g_to_e_dict = {"0": "1", "1": "0"}
    epsilon = ""
    for i in gamma:
        epsilon += g_to_e_dict[i]
    return epsilon


def calc_power_consumption(gamma: str) -> int:
    return int("0b" + gamma, 2) * int("0b" + gam_to_ep_calc(gamma), 2)


# Testing examples provided
EX_DATA = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

ex_data_list = [x.strip(" ") for x in EX_DATA.split("\n")]
ex_data_list2 = [x.strip(" ") for x in EX_DATA.split("\n")]


def test_day3_pt1():
    gam1 = get_gamma(ex_data_list)
    assert calc_power_consumption(gam1) == 198


# Test Pt 1
test_day3_pt1()

# Part 2
def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)
    return list_object


def get_ox_cycle(diag_list: List[str], gamma: str) -> List[str]:
    diag_key_length = len(gamma)
    for i in range(diag_key_length):
        digit_check = gamma[i]
        remove_idx = []
        for pos, diag in enumerate(diag_list):
            if diag[i] != digit_check:
                remove_idx.append(pos)
        diag_list = delete_multiple_element(diag_list, remove_idx)
        if len(diag_list) == 1:
            break
        gamma = get_gamma(diag_list)
    res = diag_list[0]
    return res


def get_co2_scrub(diag_list: List[str], gamma: str) -> List[str]:
    diag_key_length = len(gamma)
    for i in range(diag_key_length):
        if gamma[i] == "1":
            digit_check = "0"
        else:
            digit_check = "1"
        remove_idx = []
        for pos, diag in enumerate(diag_list):
            if diag[i] != digit_check:
                remove_idx.append(pos)
        diag_list = delete_multiple_element(diag_list, remove_idx)
        if len(diag_list) == 1:
            break
        gamma = get_gamma(diag_list)
    res = diag_list[0]
    return res


def calc_life_support_rating(o2_gen: str, co2_scrub: str) -> int:
    return int("0b" + o2_gen, 2) * int("0b" + co2_scrub, 2)


def test_day3_pt2():
    assert get_ox_cycle(ex_data_list, get_gamma(ex_data_list)) == "10111"
    assert get_co2_scrub(ex_data_list2, get_gamma(ex_data_list2)) == "01010"
    assert calc_life_support_rating("10111", "01010") == 230


# Test Pt 2
test_day3_pt2()

if __name__ == "__main__":
    with open("./inputs/will-input.txt") as f:
        input_list = [line.rstrip("\n") for line in f]

    gamma = get_gamma(input_list)
    print(f"Day 3 Part 1: {calc_power_consumption(gamma)}")

    input_list2 = list(input_list)
    ox_cycle, co2_scrub = get_ox_cycle(input_list, gamma), get_co2_scrub(
        input_list2, gamma
    )
    print(f"Day 3 Part 2: {calc_life_support_rating(ox_cycle, co2_scrub)}")
