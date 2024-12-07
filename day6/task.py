import os

STRAIGHT = 0
UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1


def read_input_file(filename):
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{curr_dir}/{filename}') as f:
        return f.read()


def char_to_row_col_dir(char):
    """ Returns ROW_DIRECTION,COL_DIRECTION """
    if char == "^":
        return UP, STRAIGHT
    if char == ">":
        return STRAIGHT, RIGHT
    if char == "<":
        return STRAIGHT, LEFT
    if char == "v":
        return DOWN, STRAIGHT


def find_start(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] in "^><v":
                return x, y


def get_visited_indexes(grid):
    indexes = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] in "X":
                indexes.append((x, y))
    return indexes


def in_bounds(grid, x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])


def build_grid(input_str):
    return [list(x.rstrip()) for x in input_str.split("\n") if x]


def simulate(grid):
    row, col = find_start(grid)
    row_dir, col_dir = char_to_row_col_dir(grid[row][col])
    visited = set()
    while in_bounds(grid, row, col):
        key = (row, col, row_dir, col_dir)
        if key in visited:
            return True  # loop detected
        else:
            visited.add(key)

        grid[row][col] = "X"

        if in_bounds(grid, row + row_dir, col + col_dir) and grid[row + row_dir][col + col_dir] in "#O":
            col_dir, row_dir = -row_dir, col_dir
        else:
            row += row_dir
            col += col_dir

    return False


def main():
    input_str = read_input_file("inputs.txt")
    grid = build_grid(input_str)
    simulate(grid)
    print("part 1 result is: ", len(get_visited_indexes(grid)))

    count_blocking = 0
    indexes_to_visit_pt_2 = get_visited_indexes(grid)
    for r, c in indexes_to_visit_pt_2:
        grid = build_grid(input_str)
        if grid[r][c] in "#^><v":
            continue
        grid[r][c] = "O"
        result = simulate(grid)
        if result:
            count_blocking += 1

    print("part 2 result is: ", count_blocking)


main()
