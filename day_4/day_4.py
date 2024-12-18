from typing import Optional


def create_srting_from_input(input_string):
    with open(input_string, mode="r") as input:
        return input.readlines()


def create_word_matrix(string_input: list[str]):
    string_data = []

    for line in string_input:
        string_line = []
        for char in line:
            string_line.append(char)
        string_data.append(string_line)
    return string_data


# horizontal, vertical, diagonal, written backwards
def scan_matrix_part1(word_matrix: list[list[str]]):
    """This function will scan the matrix data and depending on the position we're in it will look to all directions"""
    desired = "XMAS"
    finds = 0
    for index_line, line in enumerate(word_matrix):
        for index_column, _ in enumerate(line):
            finds += scan_all_directions(
                word_matrix, index_line, index_column, len(desired), desired
            )
    return finds


def scan_matrix_part2(word_matrix: list[list[str]]):
    """This function will scan the matrix data and depending on the position we're in it will look to all directions"""
    finds = 0
    for index_line, line in enumerate(word_matrix):
        for index_column, _ in enumerate(line):
            if word_matrix[index_line][index_column] == "A":
                up_forward = forward_downard_diagonal(
                    word_matrix, index_line - 1, index_column - 1, 3
                )
                down_forward = forward_upward_diagonal(
                    word_matrix, index_line + 1, index_column - 1, 3
                )

                if (
                    validate_word(up_forward, "MAS") or validate_word(up_forward, "SAM")
                ) and (
                    validate_word(down_forward, "SAM")
                    or validate_word(down_forward, "MAS")
                ):
                    finds += 1

    return finds


def scan_all_directions(word_matrix, line_index, col_index, length, desired):
    index_matches = 0
    index_matches += scan_horizontally(
        word_matrix, line_index, col_index, length, desired
    )
    index_matches += scan_vertically(
        word_matrix, line_index, col_index, length, desired
    )
    index_matches += scan_diagonally_forward(
        word_matrix, line_index, col_index, length, desired
    )
    index_matches += scan_diagonally_backwards(
        word_matrix, line_index, col_index, length, desired
    )
    return index_matches


def scan_horizontally(word_matrix, line_index, col_index, length, desired):
    index_matches = 0
    word = forward_horizontal(word_matrix, line_index, col_index, length)
    reversed_word = backward_horizontal(word_matrix, line_index, col_index, length)
    index_matches += validate_word(word, desired)
    index_matches += validate_word(reversed_word, desired)

    return index_matches


def scan_vertically(word_matrix, line_index, col_index, length, desired):
    index_matches = 0

    word = downward_vertical(word_matrix, line_index, col_index, length)
    reversed_word = upward_vertical(word_matrix, line_index, col_index, length)

    index_matches += validate_word(word, desired)
    index_matches += validate_word(reversed_word, desired)

    return index_matches


def scan_diagonally_forward(word_matrix, line_index, col_index, length, desired):
    index_matches = 0

    forward_upward_word = forward_upward_diagonal(
        word_matrix, line_index, col_index, length
    )
    forward_downward_word = forward_downard_diagonal(
        word_matrix, line_index, col_index, length
    )

    index_matches += validate_word(forward_upward_word, desired)
    index_matches += validate_word(forward_downward_word, desired)

    return index_matches


def scan_diagonally_backwards(word_matrix, line_index, col_index, length, desired):
    index_matches = 0

    backward_upward_word = backward_upward_diagonal(
        word_matrix, line_index, col_index, length
    )
    backward_downward_word = backward_downward_diagonal(
        word_matrix, line_index, col_index, length
    )

    index_matches += validate_word(backward_upward_word, desired)
    index_matches += validate_word(backward_downward_word, desired)

    return index_matches


def validate_word(word, desired):
    if word == desired:
        return True
    return False


def forward_horizontal(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    col_range = range(col_index, col_index + length)
    try:
        word = "".join([word_matrix[line_index][col] for col in col_range if col >= 0])
    except IndexError:
        word = None
    return word


def backward_horizontal(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    col_range = range(col_index, col_index - length, -1)
    try:
        word = "".join([word_matrix[line_index][col] for col in col_range if col >= 0])
    except IndexError:
        word = None
    return word


def downward_vertical(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    line_range = range(line_index, line_index + length)
    try:
        word = "".join(
            [word_matrix[line][col_index] for line in line_range if line >= 0]
        )
    except IndexError:
        word = None
    return word


def upward_vertical(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    line_range = range(line_index, line_index - length, -1)
    try:
        word = "".join(
            [word_matrix[line][col_index] for line in line_range if line >= 0]
        )
    except IndexError:
        word = None
    return word


def forward_downard_diagonal(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    line_range = range(line_index, line_index + length)
    col_range = range(col_index, col_index + length)
    try:
        word = "".join(
            [
                word_matrix[line][col]
                for (line, col) in zip(line_range, col_range)
                if line >= 0 and col >= 0
            ]
        )
    except IndexError:
        word = None

    return word


def forward_upward_diagonal(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    line_range = range(line_index, line_index - length, -1)
    col_range = range(col_index, col_index + length)
    try:
        word = "".join(
            [
                word_matrix[line][col]
                for (line, col) in zip(line_range, col_range)
                if line >= 0 and col >= 0
            ]
        )
    except IndexError:
        word = None
    return word


def backward_downward_diagonal(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    line_range = range(line_index, line_index + length)
    col_range = range(col_index, col_index - length, -1)
    try:
        word = "".join(
            [
                word_matrix[line][col]
                for (line, col) in zip(line_range, col_range)
                if line >= 0 and col >= 0
            ]
        )
    except IndexError:
        word = None
    return word


def backward_upward_diagonal(
    word_matrix,
    line_index: int,
    col_index: int,
    length: int,
):
    line_range = range(line_index, line_index - length, -1)
    col_range = range(col_index, col_index - length, -1)
    try:
        word = "".join(
            [
                word_matrix[line][col]
                for (line, col) in zip(line_range, col_range)
                if line >= 0 and col >= 0
            ]
        )
    except IndexError:
        word = None
    return word


def get_single_char(
    word_matrix,
    line_index: int,
    col_index: int,
):
    line_index = line_index
    col_index = col_index
    try:
        word = "".join([word_matrix[line_index][col_index]])
    except IndexError:
        word = None
    return word


data = create_srting_from_input("day_4_input.txt")
word_matrix = create_word_matrix(data)
results_part_1 = scan_matrix_part1(word_matrix)
results_part_2 = scan_matrix_part2(word_matrix)
print(f"The total number of XMAS findings is {results_part_1}")
print(f"The total number of X-MAS findings is {results_part_2}")
