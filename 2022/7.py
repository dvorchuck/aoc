input = open("input_7.txt").read()
input_v2 = input.split('\n')

directory = {}  # this is the /
curr_path = []
curr_dir = directory  # current directory, works as a pointer


def goto_home_directory():
    global curr_dir
    global curr_path

    curr_dir = directory
    curr_path = []


def goto_directory(name):  # in current path
    global curr_dir
    global curr_path

    curr_dir = curr_dir[name]
    curr_path.append(name)


def goto_parent_directory():
    global curr_path
    global curr_dir
    curr_path = curr_path[:-1]

    if len(curr_path) == 0:
        goto_home_directory()

    curr_dir = directory

    for step in curr_path:
        curr_dir = curr_dir[step]


def add_directory(name):  # in current path
    curr_dir[name] = {}


def add_file(size, name):
    curr_dir[name] = int(size)


# build map
for row in input_v2:
    parts = row.split(' ')
    if parts[0] == '$':  # is command input

        if parts[1] == 'ls':
            continue

        elif parts[1] == 'cd':
            if parts[2] == '/':
                goto_home_directory()
            elif parts[2] == '..':
                goto_parent_directory()
            else:
                goto_directory(parts[2])

    elif parts[0] == 'dir':
        add_directory(parts[1])
    else:
        add_file(parts[0], parts[1])


def get_directory_size(directory: dict):
    size = 0
    for value in directory.values():
        if isinstance(value, int):
            size += value
        else:

            size += get_directory_size(value)

    return size


def part1():
    total = 0
    stack = []
    stack.extend(directory.values())
    for value in stack:
        if isinstance(value, int):
            continue
        else:
            stack.extend(value.values())
            size = get_directory_size(value)
            if size <= 100000:
                total += size

    return total


def part2():
    stack = []
    stack.extend(directory.values())
    result = []
    for value in stack:
        if isinstance(value, int):
            continue
        else:
            stack.extend(value.values())
            size = get_directory_size(value)
            if size >= 30000000 - (70000000 - get_directory_size(directory)):
                result.append(size)

    return min(result)
