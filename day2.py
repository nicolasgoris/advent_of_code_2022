import sys


def calc_points(pOne, pTwo):
    points = 1 if pTwo == "X" else 2 if pTwo == "Y" else 3
    points += (
        6
        if pOne == "A"
        and pTwo == "Y"
        or pOne == "B"
        and pTwo == "Z"
        or pOne == "C"
        and pTwo == "X"
        else 3
        if pOne == "A"
        and pTwo == "X"
        or pOne == "B"
        and pTwo == "Y"
        or pOne == "C"
        and pTwo == "Z"
        else 0
    )
    return points


def get_dict(part):
    if part == 1:
        return dict()
    if part == 2:
        return dict(
            [
                ("AX", 3),
                ("BX", 1),
                ("CX", 2),
                ("AY", 4),
                ("BY", 5),
                ("CY", 6),
                ("AZ", 8),
                ("BZ", 9),
                ("CZ", 7),
            ]
        )


def part1(games):
    result = 0
    for i, game in enumerate(games):
        result += calc_points(game[0], game[1])
    return result


def part2(games):
    pdict = get_dict(2)
    result = 0
    for i, game in enumerate(games):
        result += pdict[game[0] + game[1]]
    return result


assert len(sys.argv) == 2
games = list(map(lambda g: g.split(" "), open(sys.argv[1]).read().splitlines()))
print(f"Part 1: {part1(games)} - Part 2: {part2(games)}")
