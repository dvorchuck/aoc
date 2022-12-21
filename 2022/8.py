input = open("input_8.txt").read()
input_v2 = input.split('\n')

data = []

for row in input_v2:
    line = []

    line.extend(row)
    line = list(map(lambda x: int(x), line))
    data.append(line)


def is_visible(row, col):
    # edge top or left
    if row == 0 or col == 0:
        return True
    # edge right or botton
    if row == len(data[0]) - 1 or col == len(data) - 1:
        return True

    curr = data[row][col]
    curr_row = data[row]
    curr_col = list(map(lambda row: row[col], data))

    # # visible from left
    if curr > max(curr_row[:col]):
        return True

    # # visible from right
    if curr > max(curr_row[col + 1:]):
        return True

    #  # visible from top
    if curr > max(curr_col[:row]):
        return True

    # # visible from bottom
    if curr > max(curr_col[row + 1:]):
        return True

    return False


def line_score(cur, line):
    score = 0
    for tree in line:
        if cur > tree:
            score += 1
        else:
            score += 1
            break
    return score


def score(row, col):
    if row == 0 or col == 0:
        return 0
    # edge right or botton
    if row == len(data[0]) - 1 or col == len(data) - 1:
        return 0

    curr = data[row][col]
    curr_row = data[row]
    curr_col = list(map(lambda row: row[col], data))

    # # visible from left
    left_line = curr_row[:col]
    left_line.reverse()
    left = line_score(curr, left_line)

    # # visible from right
    right_line = curr_row[col + 1:]
    right = line_score(curr, right_line)

    #  # visible from top
    top_line = curr_col[:row]
    top_line.reverse()
    top = line_score(curr, top_line)

    # # visible from bottom
    bottom_line = curr_col[row + 1:]
    bottom = line_score(curr, bottom_line)
    score = left * top * right * bottom
    return score


def part1():
    total = 0
    for i, row in enumerate(data):
        for id, tree in enumerate(row):
            if is_visible(i, id):
                total += 1
    return total


def part2():
    highest = 0
    for i, row in enumerate(data):
        for id, tree in enumerate(row):
            if score(i, id) > highest:
                highest = score(i, id)

    return highest

