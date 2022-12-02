def get_lines():
    with open("input documents/input day 2.1.txt", "r") as file:
        return file.readlines()


def iterate_over_games(lines):
    score = 0
    for line in lines:
        score = add_element_to_score(line[2], score)
        score = add_result_to_score(line, score)
    return score


def add_element_to_score(element: str, score: int):
    return score + points[element]


def add_result_to_score(line, score):
    return score + determine_result(line)


def determine_result(line):
    return points[get_element(line[2], line[0])]


def get_element(result, element):
    if (result == "X" and element == "B") or (result == "Y" and element == "A") or (result == "Z" and element == "C"):
        return "A"
    if (result == "X" and element == "C") or (result == "Y" and element == "B") or (result == "Z" and element == "A"):
        return "B"
    return "C"



points = {
    "X": 0,
    "Y": 3,
    "Z": 6,
    "A": 1,
    "B": 2,
    "C": 3
}


if __name__ == "__main__":
    print(iterate_over_games(get_lines()))