import os


def read_input_file(filename):
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{curr_dir}/{filename}') as f:
        return f.readlines()


def process_rules():
    rules = [rule.strip().split("|") for rule in read_input_file("rules.txt")]
    return [(int(x), int(y)) for x, y in rules]


def process_updates():
    updates = [line.strip().split(",") for line in read_input_file("updates.txt")]
    return [[int(y) for y in x] for x in updates]


def check_valid(rules, update):
    for x, y in rules:
        if x in update and y in update and update.index(x) > update.index(y):
            return False
    return True


def reorder(rules, update):
    # Bubble sort-esque reorder
    ordered = False
    while not ordered:
        ordered = True

        for x, y in rules:
            if x not in update or y not in update:
                continue

            x_idx = update.index(x)
            y_idx = update.index(y)
            if x_idx > y_idx:
                update[x_idx], update[y_idx] = update[y_idx], update[x_idx]
                ordered = False
    return update


def main():
    rules = process_rules()
    valid, invalid = [], []

    for update in process_updates():
        if check_valid(rules, update):
            valid.append(update)
        else:
            invalid.append(update)

    # Task 1
    total_middle = 0
    for val in valid:
        total_middle += val[len(val) // 2]
    print('Valid middles:', total_middle)

    # Task 2
    total_middle_invalid = 0
    for val in invalid:
        reordered = reorder(rules, val)
        total_middle_invalid += reordered[len(val) // 2]
    print('Invalid middles:', total_middle_invalid)


main()
