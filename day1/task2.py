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

    return arr1, arr2


def get_similarity_score(arr1, arr2_counter):
    cumulative_score = 0
    for item in arr1:
        cumulative_score += item * arr2_counter[item]
    return cumulative_score


def main():
    arr1, arr2 = load_input()
    arr2_counted = Counter(arr2)
    sim_score = get_similarity_score(arr1, arr2_counted)
    print('similarity score is:', sim_score)
    return sim_score


if __name__ == '__main__':
    main()
