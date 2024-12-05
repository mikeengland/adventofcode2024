import os
import re

MUL_REGEX = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
DO_DONT_REGEX = r"do\(\)([\s\S]*?)(?:don\'t\(\))"


def read_input():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{curr_dir}/input.txt') as f:
        return f.read()


def process_muls(mul_str):
    matches = re.findall(MUL_REGEX, mul_str)
    total = 0
    for val1, val2 in matches:
        total += int(val1) * int(val2)
    return total


def process_with_do_dont(mul_str):
    # Process first part of string before the first do() as these are enabled
    before_first_do = mul_str.index('do()')
    total = process_muls(mul_str[:before_first_do])
    # Process string between do() and don't()
    matches = re.findall(DO_DONT_REGEX, mul_str)
    for match in matches:
        total += process_muls(match)
    # Process last do() if present
    last_do = mul_str.rfind("do()")
    if last_do == -1 or "don't()" in mul_str[last_do:]:
        return total

    return total + process_muls(mul_str[last_do:])


if __name__ == "__main__":
    text = read_input()
    total = process_muls(text)
    print("Total: ", total)
    total = process_with_do_dont(text)
    print("Total with Do Don't: ", total)