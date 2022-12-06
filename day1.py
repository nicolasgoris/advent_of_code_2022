import sys


def part1(list):
    elves = [0]
    for i in list:
        if len(i) > 0:
            elves.append(elves.pop() + int(i))
        else:
            elves.append(0)
    return max(elves)


def part2(list):
    elves = [0]
    for i in list:
        if len(i) > 0:
            elves.append(elves.pop() + int(i))
        else:
            elves.append(0)
    top_three = 0
    for i in range(3):
        index = elves.index(max(elves))
        top_three += elves.pop(index)
    return top_three


assert len(sys.argv) == 2
list = open(sys.argv[1]).read().splitlines()
print(f"Part 1: {part1(list)} - Part 2: {part2(list)}")
