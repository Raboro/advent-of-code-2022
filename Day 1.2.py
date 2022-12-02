with open("input documents/input day 1.1.txt", "r") as file:
    lines = file.readlines()

elves = []

elf = 0
highest_value = [0, 0]
for line in lines:
    if line == "\n":
        if highest_value[0] < elf:
            highest_value[0] = elf
            highest_value[1] = len(elves)
        elves.append(elf)
        elf = 0
        continue
    elf += int(line)

value = highest_value[0]


def get_next_highest_value(elves):
    elves.remove(max(elves))
    return max(elves)


value += get_next_highest_value(elves)
value += get_next_highest_value(elves)

print(f"Value of the three Elves carrying the most: {value}")
