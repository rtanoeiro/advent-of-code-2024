def create_lists_from_input(input_string):
    report_list = []

    with open(input_string, mode="r") as input:
        string_data = input.readlines()

    for line in string_data:
        values = line.split()
        report_list.append(values)

    return report_list


def count_report_safety(report_list):
    safety_reports = []
    for level_list in report_list:
        level_list: list
        safety_combination = []
        for item in level_list:
            level_list_copy = level_list.copy()
            level_list_copy.remove(item)
            if evaluate_safety(level_list_copy):
                safety_combination.append("safe")
                break
            else:
                safety_combination.append("unsafe")
        if "safe" in safety_combination:
            safety_reports.append("safe")
        else:
            safety_reports.append("unsafe")

    return safety_reports


def check_only_increasing(level_list: list):
    state = []
    level_list_size = len(level_list) - 1

    # If the list is decreasing, we force it as increasing
    if int(level_list[0]) > int(level_list[1]):
        level_list.reverse()

    for index, _ in enumerate(level_list):
        if index == level_list_size:  # stop at the last number
            break

        if int(level_list[index]) < int(level_list[index + 1]):
            state.append("safe")
        else:
            state.append("unsafe")

    return state


def check_only_one_up_to_three_levels(level_list):
    state = []
    level_list_size = len(level_list) - 1
    for index, _ in enumerate(level_list):
        if index == level_list_size:  # stop at the last number
            break

        if abs(int(level_list[index]) - int(level_list[index + 1])) in [1, 2, 3]:
            state.append("safe")
        else:
            state.append("unsafe")

    return state


def evaluate_safety(level_list):
    increasing_safety = check_only_increasing(level_list)
    level_change_safety = check_only_one_up_to_three_levels(level_list)

    is_safe_increase = (
        len(list(filter(lambda safety: safety == "unsafe", increasing_safety))) == 0
    )
    is_safe_change = (
        len(list(filter(lambda safety: safety == "unsafe", level_change_safety))) == 0
    )

    return is_safe_increase and is_safe_change


report_list = create_lists_from_input("day_2_input.txt")
results = count_report_safety(report_list)
safe_results = len(list(filter(lambda safe: safe == "safe", results)))
print(f"There are a total of {safe_results} safe levels")
