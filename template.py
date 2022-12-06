import sys


def part1(list):
    print(list)
    return 0


def part2(list):
    return 0


assert len(sys.argv) == 2
list = open(sys.argv[1]).read().splitlines()
print(f"Part 1: {part1(list)} - Part 2: {part2(list)}")
