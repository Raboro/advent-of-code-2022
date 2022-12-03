def get_input():
    with open("input documents/input day 3.1.txt", "r") as file:
        return file.readlines()


def get_groups(lines):
    groups = []
    group = []
    for index, line in enumerate(lines):
        if index % 3 == 0 and index != 0:
            groups.append(group)
            group = []
        group.append(line)
    groups.append(group)
    return groups


def iterate_over_groups(groups):
    result = 0
    for group in groups:
        item = get_duplicated_item(group)
        result += get_item_priority(item)
    return result


def get_duplicated_item(group):
    for backpack_one in group[0]:
        for backpack_two in group[1]:
            for backpack_three in group[2]:
                if backpack_one == backpack_two and backpack_two == backpack_three:
                    return backpack_three


def get_item_priority(item):
    return priority[item] if item.islower() else priority[item.lower()] + 26


priority = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}


if __name__ == "__main__":
    print(iterate_over_groups(get_groups(get_input())))
