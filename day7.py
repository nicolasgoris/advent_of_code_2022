import sys, re, json


rcmd = r"\$ ([A-z]{2}) *([/.A-z]+)*"
rdir = r"dir ([A-z]*)"
rfile = r"(\d+) ([A-z]+(.[A-z])*)"

# fs = {"name": "/", "dir": [{"name": "a", "dir": [], "size": 0}]}


def read_instr(fs, instr):
    cmd = re.search(rcmd, instr)
    if cmd:
        fs["prev"] = cmd.group(1)
        if cmd.group(1) == "cd":
            if cmd.group(2) == "/":
                fs = {"name": "/", "dir": [], "sizez": 0}
                fs["path"] = cmd.group(2)
            elif cmd.group(2) == "..":
                fs["path"] = fs["path"].rsplit("/", 2)[0] + "/"
                # fs["path"] = "/" if fs["path"] == "" else fs["path"]
                # {"name": cmd.group(2), "size": 0, "sub": {}}
            else:
                fs["path"] = fs["path"] + cmd.group(2) + "/"
                fs["root"][cmd.group(2)] = {}
        if cmd.group(1) == "ls":
            fs["path"] = fs["path"]
    # dir = re.search(rdir, instr)
    # file = re.search(rfile, instr)
    else:
        file = re.search(rfile, instr)
        if file:
            print("jups")
    return fs


def part1(instructions):
    fs = {}
    for i in instructions:
        print(i)
        fs = read_instr(fs, i)
        print(fs)
    print(instructions)
    return 0


def part2(list):
    return 0


assert len(sys.argv) == 2
input = open(sys.argv[1]).read().splitlines()
print(f"Part 1: {part1(input)} - Part 2: {part2(input)}")
