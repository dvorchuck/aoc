input = open("input_10.txt").read()
input_v2 = input.split('\n')

data = []
X = 1
cycle_data = []


def fill_data():
    for row in input_v2:

        if row == 'noop':
            data.append(0)
            continue

        command, value = row.split(' ')

        data.append(int(value))


fill_data()


def calculate_cycles():
    global X
    for row in data:
        cycle_data.append(X)

        if row == 0:
            continue

        cycle_data.append(X)
        X += row

    return


calculate_cycles()


def part1():
    total = 0
    for id, value in enumerate(cycle_data):
        if (id + 21) % 40 == 0:
            total += (id + 1) * value

    return total


# part1()
def part2():
    pixels = ''

    for id, value in enumerate(cycle_data):

        position = id % 40
        if position == 0:
            pixels += '\n'
            
        if position >= value - 1 and position <= value + 1:
            pixels += '#'
        else:
            pixels += '.'

    return pixels.split('\n')


part2()
