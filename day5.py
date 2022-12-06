import sys


def create_stack(list):
    nrRows = len(list) - 2
    nrCols = int(max(list[nrRows]))
    stack = []
    row, col = 0, 0
    while col < nrCols:
        stack.append([])
        while row < nrRows:
            char = list[row][col * 4 + 1]
            if char != " ":
                currCol = stack.pop()
                currCol.append(char)
                stack.append(currCol)
            row += 1
        row = 0
        col += 1
    col = 0
    while col < nrCols:
        stack[col] = stack[col][::-1]
        col += 1
    return stack


def execute_move_9000(stack, move):
    i = 0
    while i < move[0]:
        item = stack[move[1]].pop()
        stack[move[2]].append(item)
        i += 1
    return stack


def execute_move_9001(stack, move):
    i = 0
    size = len(stack[move[1]])
    stay, lift = (
        stack[move[1]][0 : size - move[0]],
        stack[move[1]][size - move[0] : size],
    )
    print(stay, lift)
    stack[move[1]] = stay
    stack[move[2]].extend(lift)
    print(stack)
    return stack


def create_moves(list):
    moves = []
    for i in list:
        instr = []
        temp = "".join(i.split()).split("move")[1].split("from")
        instr.append(int(temp[0]))
        instr.append(int(temp[1].split("to")[0]) - 1)
        instr.append(int(temp[1].split("to")[1]) - 1)
        moves.append(instr)
    return moves


def part1(input):
    raw_stack, raw_moves = (
        input[: input.index("move")].splitlines(),
        input[input.index("move") :].splitlines(),
    )
    stack, moves = create_stack(raw_stack), create_moves(raw_moves)
    for m in moves:
        stack = execute_move_9000(stack, m)
    result = ""
    for s in stack:
        result += s.pop()
    return result


def part2(list):
    raw_stack, raw_moves = (
        input[: input.index("move")].splitlines(),
        input[input.index("move") :].splitlines(),
    )
    stack, moves = create_stack(raw_stack), create_moves(raw_moves)
    for m in moves:
        stack = execute_move_9001(stack, m)
    result = ""
    for s in stack:
        result += s.pop()
    return result


assert len(sys.argv) == 2
input = open(sys.argv[1]).read()
# list(map(lambda g: g.split(' '), open(sys.argv[1]).read().splitlines()))
print(f"Part 1: {part1(input)} - Part 2: {part2(input)}")
