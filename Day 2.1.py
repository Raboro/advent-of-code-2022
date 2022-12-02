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
    return score + points[determine_result(line)]


def determine_result(line):
    opponent = line[0]
    player = line[2]
    if (opponent == "A" and player == "Y") or (opponent == "B" and player == "Z") or (opponent == "C" and player == "X"):
        return "W"
    if (opponent == "A" and player == "X") or (opponent == "B" and player == "Y") or (opponent == "C" and player == "Z"):
        return "D"
    return "L"


points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "W": 6,
    "D": 3,
    "L": 0
}


if __name__ == "__main__":
    print(iterate_over_games(get_lines()))