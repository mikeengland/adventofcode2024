import os

MIN_DIFF = 1
MAX_DIFF = 3


def read_input():
    reports = []
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{curr_dir}/input.txt') as f:
        for line in f:
            reports.append([int(x) for x in line.strip().split(' ')])

    return reports


def is_report_valid(report: list[int]) -> bool:
    asc = report[0] < report[1]

    for i in range(1, len(report)):
        num, prev_num = report[i], report[i-1]
        if not MIN_DIFF <= abs(num - prev_num) <= MAX_DIFF:
            return False

        if asc and num < prev_num or not asc and num > prev_num:
            return False

    return True


def is_report_valid_with_removals(report: list[int]) -> bool:
    for i in range(len(report)):
        without_one_level = report[:i] + report[i + 1:]
        if is_report_valid(without_one_level):
            return True
    return False


def main():
    reports = read_input()
    print("Part 1: number of reports that are valid: ", sum(int(is_report_valid(report)) for report in reports))
    print(
        "Part 2: number of reports that are valid with removals: ",
        sum(int(is_report_valid_with_removals(report)) for report in reports)
    )


if __name__ == '__main__':
    main()
