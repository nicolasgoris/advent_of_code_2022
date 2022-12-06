import sys, re, functools
from collections import Counter

reg = r"(\d+)-(\d+),(\d+)-(\d+)"


def checkFullOverlap(pair):
    match = re.search(reg, pair)
    a, b, c, d = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
    )
    return a <= c and b >= d or c <= a and d >= b


def checkOverlap(pair):
    match = re.search(reg, pair)
    a, b, c, d = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
    )
    return b >= c and d >= a


def part1(input):
    count = 0
    overlap = list(map(checkFullOverlap, input))
    for i in overlap:
        if i:
            count += 1
    return count


def part2(input):
    count = 0
    overlap = list(map(checkOverlap, input))
    for i in overlap:
        if i:
            count += 1
    return count


assert len(sys.argv) == 2
input = open(sys.argv[1]).read().splitlines()
print(f"Part 1: {part1(input)} - Part 2: {part2(input)}")
