import sys
from collections import Counter


def isUniqueChars(string):
    # Counting frequency
    freq = Counter(string)
    if len(freq) == len(string):
        return True
    else:
        return False


def part1(list):
    i = 3
    while i < len(list):
        check = list[i - 3 : i + 1]
        if isUniqueChars(check):
            return i + 1
        i += 1
    return 0


def part2(list):
    i = 13
    while i < len(list):
        check = list[i - 13 : i + 1]
        if isUniqueChars(check):
            return i + 1
        i += 1
    return 0


assert len(sys.argv) == 2
list = open(sys.argv[1]).read()
print(f"Part 1: {part1(list)} - Part 2: {part2(list)}")
