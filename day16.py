import re

def get_size(path):
    size = 0
    for line in path:
        if line.startswith('dir'):
            size += get_size(path)
        else:
            size += int(line.split()[0])
    return size

def main():
    with open('ex7.txt') as f:
        path = []
        for line in f:
            if line.startswith('$'):
                command = line.split()
                if command[1] == 'cd':
                    if command[2] == '/':
                        path = []
                    elif command[2] == '..':
                        path.pop()
                    else:
                        path.append(command[2])
                elif command[1] == 'ls':
                    size = get_size(path)
                    if size <= 100000:
                        print(path, size)

if __name__ == '__main__':
    main()