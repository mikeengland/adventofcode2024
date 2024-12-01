import os


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


def main():
    arr1, arr2 = load_input()
    summed_diff = get_sorted_diff(arr1, arr2)
    print('summed diff is:', summed_diff)
    return summed_diff


if __name__ == '__main__':
    main()

