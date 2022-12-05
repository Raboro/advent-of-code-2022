from Input import Input

elves = []

elf = 0
highest_value = [0, 0]
for line in Input.get_input_of_file("input documents/input day 1.1.txt"):
    if line == "\n":
        if highest_value[0] < elf:
            highest_value[0] = elf
            highest_value[1] = len(elves)
        elves.append(elf)
        elf = 0
        continue
    elf += int(line)

print(f"Elf: {highest_value[1]} has the highest value: {highest_value[0]}")