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
    matrix_size = len(word_matrix)
    length = len("XMAS")
    finds = 0
    for index_line, line in enumerate(word_matrix):
        if index_line != matrix_size - 1:
            # All lines have a line break by default, except the last one
            line.remove("\n")
        for index_column, _ in enumerate(line):
            finds += scan_all_directions(word_matrix, index_line, index_column, length)
    return finds


def scan_matrix_part2(word_matrix: list[list[str]]):
    """This function will scan the matrix data and depending on the position we're in it will look to all directions"""
    matrix_size = len(word_matrix)
    finds = 0
    length = len("A")
    for index_line, line in enumerate(word_matrix):
        if index_line != matrix_size - 1:
            # All lines have a line break by default, except the last one
            line.remove("\n")
        for index_column, _ in enumerate(line):
            if word_matrix[index_line][index_column] == "A"

                finds += scan_diagonally(word_matrix, index_line, index_column, length)
    
    return finds


def scan_all_directions(word_matrix, line_index, col_index, length, desired):
    index_matches = 0
    index_matches += scan_horizontally(word_matrix, line_index, col_index, length, desired)
    index_matches += scan_vertically(word_matrix, line_index, col_index, length, desired)
    index_matches += scan_diagonally(word_matrix, line_index, col_index, length, desired)
    return index_matches


def scan_horizontally(word_matrix, line_index, col_index, length, desired):
    index_matches = 0
    word = forward_horizontal(word_matrix, line_index, col_index, length)
    reversed_word = backward_horizontal(word_matrix, line_index, col_index, length)
    index_matches += validate_word(word, desired)
    index_matches += validate_word(reversed_word,desired)

    return index_matches


def scan_vertically(word_matrix, line_index, col_index, length, desired):
    index_matches = 0

    word = downward_vertical(word_matrix, line_index, col_index, length)
    reversed_word = upward_vertical(word_matrix, line_index, col_index, length)

    index_matches += validate_word(word, desired)
    index_matches += validate_word(reversed_word, desired)

    return index_matches


def scan_diagonally(word_matrix, line_index, col_index, length, desired):
    index_matches = 0

    forward_upward_word = forward_upward_diagonal(
        word_matrix, line_index, col_index, length
    )
    forward_downward_word = forward_downard_diagonal(
        word_matrix, line_index, col_index, length
    )
    backward_upward_word = backward_upward_diagonal(
        word_matrix, line_index, col_index, length
    )
    backward_downward_word = backward_downward_diagonal(
        word_matrix, line_index, col_index, length
    )

    index_matches += validate_word(forward_upward_word, desired)
    index_matches += validate_word(forward_downward_word, desired)
    index_matches += validate_word(backward_upward_word, desired)
    index_matches += validate_word(backward_downward_word, desired)

    return index_matches


def validate_word(word, desired):
    if word == desired:
        return 1
    return 0


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
    lenght: int,
):
    line_range = range(line_index, line_index - lenght, -1)
    col_range = range(col_index, col_index - lenght, -1)
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


data = create_srting_from_input("day_4_input.txt")
word_matrix = create_word_matrix(data)
# word_matrix = word_matrix[:12]
results_part_1 = scan_matrix_part1(word_matrix)
results_part_2 = scan_matrix_part2(word_matrix)
print(f"The total number of XMAS findings is {results_part_1}")
