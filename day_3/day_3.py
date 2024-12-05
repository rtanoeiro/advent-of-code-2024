import re


def create_srting_from_input(input_string):
    with open(input_string, mode="r") as input:
        return input.read()


def get_valid_multiplications(string):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, string)


def get_valid_multiplications_part2(string):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|\bdo(?:n't)?\b"
    return re.findall(pattern, string)


def mul(x, y):
    return x * y


def multiply_and_sum(mul_list: list[str]):
    sum = 0
    for item in mul_list:
        item = item.replace("(", "").replace(")", "").replace("mul", "")
        numbers = item.split(",")
        sum += mul(int(numbers[0]), int(numbers[1]))
    return sum


def multiply_and_sum_part2(mul_list: list[str]):
    sum = 0
    do = True
    for item in mul_list:
        if item == "don't":
            do = False
            continue

        if item == "do":
            do = True
            continue

        if do:
            sum += multiply_and_sum([item])

    return sum


string_data = create_srting_from_input("day_3_input.txt")
finds = get_valid_multiplications(string_data)
finds_part2 = get_valid_multiplications_part2(string_data)
results = multiply_and_sum(finds)
print(f"The first part 1 results is {results}")
results_part2 = multiply_and_sum_part2(finds_part2)
print(f"The first part 2 results is {results_part2}")
