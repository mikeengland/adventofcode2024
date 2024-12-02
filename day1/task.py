import os
from collections import Counter


def load_input():
    arr1, arr2 = [], []

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{curr_dir}/input.txt') as f:
        for line in f:
            item1, item2 = line.split('   ')
            arr1.append(int(item1.strip()))
            arr2.append(int(item2.strip()))

    return sorted(arr1), sorted(arr2)


def get_sorted_diff(arr1, arr2):
    total_diff = 0
    for a, b in zip(arr1, arr2):
        total_diff += abs(a - b)
    return total_diff


def get_similarity_score(arr1, arr2_counter):
    cumulative_score = 0
    for item in arr1:
        cumulative_score += item * arr2_counter[item]
    return cumulative_score


def main():
    arr1, arr2 = load_input()
    print('Part 1: summed diff is:', get_sorted_diff(arr1, arr2))
    print('Part 2: similarity score is:', get_similarity_score(arr1, Counter(arr2)))


if __name__ == '__main__':
    main()

