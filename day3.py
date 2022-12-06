import sys


def part1(list):
    prio = []
    for i in list:
        half_length = len(i) // 2
        first_half, second_half = i[:half_length], i[half_length:]
        common = set.intersection(*map(set, [first_half, second_half]))
        prio.append(
            [ord(char) - (96 if ord(char) > 95 else (64 - 26)) for char in common][0]
        )
    return sum(prio)


def part2(list):
    prio = []
    i = 0
    while i < len(list):
        common = set.intersection(*map(set, [list[i], list[i + 1], list[i + 2]]))
        prio.append(
            [ord(char) - (96 if ord(char) > 95 else (64 - 26)) for char in common][0]
        )
        i += 3
    return sum(prio)


assert len(sys.argv) == 2
list = open(sys.argv[1]).read().splitlines()
print(f"Part 1: {part1(list)} - Part 2: {part2(list)}")
