import os


def input_example():
    return [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]


def read_input_file():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{curr_dir}/input.txt') as f:
        return f.readlines()


class Day4:
    DIR_RIGHT = 1
    DIR_LEFT = -1
    DIR_UP = -1
    DIR_DOWN = 1
    DIR_STRAIGHT = 0

    def __init__(self, input_lines: list[str], word):
        self.word = word
        self.grid = [list(line) for line in input_lines]

    def find_word(self, row, col, row_direction, col_direction):
        for i in range(len(self.word)):
            if row < 0 or row >= len(self.grid):
                return 0
            if col < 0 or col >= len(self.grid[0]):
                return 0
            if self.grid[row][col] != self.word[i]:
                return 0

            row += row_direction
            col += col_direction

        return 1

    def task1(self):
        """ For each element, check for the word in each direction (inc diagonals) and count number of words found """
        count = 0

        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                count += self.find_word(row, col, self.DIR_STRAIGHT, self.DIR_RIGHT)  # right
                count += self.find_word(row, col, self.DIR_STRAIGHT, self.DIR_LEFT)  # left
                count += self.find_word(row, col, self.DIR_DOWN, self.DIR_STRAIGHT)  # down
                count += self.find_word(row, col, self.DIR_UP, self.DIR_STRAIGHT)  # up
                count += self.find_word(row, col, self.DIR_DOWN, self.DIR_LEFT)  # diagonally down left
                count += self.find_word(row, col, self.DIR_DOWN, self.DIR_RIGHT)  # diagonally down right
                count += self.find_word(row, col, self.DIR_UP, self.DIR_LEFT)  # diagonally up left
                count += self.find_word(row, col, self.DIR_UP, self.DIR_RIGHT)  # diagonally up right

        return count

    def task2(self):
        """ Check """
        total = 0
        for row in range(1, len(self.grid)):
            for col in range(1, len(self.grid[0])):
                result = (
                    self.find_word(row + self.DIR_UP, col + self.DIR_LEFT, self.DIR_DOWN, self.DIR_RIGHT) +
                    self.find_word(row + self.DIR_UP, col + self.DIR_RIGHT, self.DIR_DOWN, self.DIR_LEFT) +
                    self.find_word(row + self.DIR_DOWN, col + self.DIR_LEFT, self.DIR_UP, self.DIR_RIGHT) +
                    self.find_word(row + self.DIR_DOWN, col + self.DIR_RIGHT, self.DIR_UP, self.DIR_LEFT)
                )
                # if 2 then both diagonals have been found making the X shape
                if result == 2:
                    total += 1
        return total


if __name__ == "__main__":
    inputs = read_input_file()
    # inputs = input_example()
    total = Day4(inputs, "XMAS").task1()
    print("Part 1 total is: ", total)
    total = Day4(inputs, "MAS").task2()
    print("Part 2 total is: ", total)
