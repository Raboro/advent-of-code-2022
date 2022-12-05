from Input import Input


def iterate_over_lines(lines):
    result = 0
    for line in lines:
        item = get_duplicated_item(line)
        result += get_item_priority(item)
    return result


def get_duplicated_item(line):
    splitted_line = get_splitted_line(line)
    for char in splitted_line[0]:
        for compare in splitted_line[1]:
            if char == compare:
                return char


def get_splitted_line(line):
    split_index = len(line) // 2
    return [line[slice(0, split_index)], line[slice(split_index, len(line) - 1)]]


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
    print(iterate_over_lines(Input.get_input_of_file("input documents/input day 3.1.txt")))
