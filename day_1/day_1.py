def create_lists_from_input(input_string):
    list1, list2 = [], []

    with open(input_string, mode="r") as input:
        string_data = input.readlines()

    for line in string_data:
        values = line.split()
        list1.append(int(values[0]))
        list2.append(int(values[1]))

    return list1, list2


def calculate_differences_between_two_lists(list1, list2):
    distance = 0
    for num1, num2 in zip(list1, list2):
        distance += abs(num1 - num2)
    return distance


def map_list_numbers(list):
    mapped_dict = {}
    for item in list:
        if item in mapped_dict:
            mapped_dict[item] += 1
        else:
            mapped_dict[item] = 1
    return mapped_dict


def calculate_similarity_score(input_list, input_dict):
    similarity_score = 0
    for item in input_list:
        if item in input_dict:
            similarity_score += item * input_dict[item]

    return similarity_score


list1, list2 = create_lists_from_input("day_1_input.txt")
distance = calculate_differences_between_two_lists(sorted(list1), sorted(list2))
print(f"The total distance from the two lists is {distance}")
mapped_list = map_list_numbers(list2)
similarity_score = calculate_similarity_score(list1, mapped_list)
print(f"The similarity score is: {similarity_score}")
