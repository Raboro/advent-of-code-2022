from Input import Input


def get_sections(elves: list):
    sections = []
    for elf in elves:
        sections.append(get_boarder_numbers(elf, sections))
    return sections


def get_boarder_numbers(elf: str, sections):
    elf = elf.split(",")
    sections.append(get_range(elf[0]))
    sections.append(get_range(elf[1]))
    return sections


def get_range(elf: str):
    elf = elf.split("-")
    return "".join(str([i for i in range(int(elf[0]), int(elf[1]))]))


if __name__ == "__main__":
    sections = get_sections(Input.get_input_of_file("input documents/input day 4.1.txt"))
