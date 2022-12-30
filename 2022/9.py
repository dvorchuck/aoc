from typing import Literal

input = open("input_9.txt").read()
input_v2 = input.split('\n')

DIRECTION = Literal['U', 'D', 'L', 'R']

# init start
plan = {}

# plan[row x col]
plan['0x0'] = {
    'head_visit': 1,
    'tail_visit': 1,
}

tail = {
    'row': 0,
    'col': 0,
}

head = {
    'row': 0,
    'col': 0,
}


def add_visit(row: int, col: int, type: Literal['head', 'tail']):
    position = f'{row}x{col}'

    if not position in plan:
        plan[position] = {'head_visit': 0,
                          'tail_visit': 0, }

    plan[position][f'{type}_visit'] += 1


def is_tail_separate():
    if abs(head['row'] - tail['row']) <= 1 and abs(head['col'] - tail['col']) <= 1:
        return False


def move(direction: DIRECTION):

    # move head
    match direction:
        case 'U':
            head['row'] += 1
        case 'D':
            head['row'] -= 1
        case 'R':
            head['col'] += 1
        case 'L':
            head['col'] -= 1

    add_visit(head["row"], head["col"], 'head')

    # tail movement is not needed
    if abs(head['row'] - tail['row']) <= 1 and abs(head['col'] - tail['col']) <= 1:
        return

    # move tail
    match direction:
        case 'U':
            tail['row'] += 1
            tail['col'] = head['col']
        case 'D':
            tail['row'] -= 1
            tail['col'] = head['col']
        case 'R':
            tail['col'] += 1
            tail['row'] = head['row']
        case 'L':
            tail['col'] -= 1
            tail['row'] = head['row']

    add_visit(tail["row"], tail["col"], 'tail')


def simulate_movement():
    for line in input_v2:
        direction, rept = line.split(' ')
        rept = int(rept)
        for x in range(rept):
            move(direction)


def part1():
    total = 0

    for key in plan.keys():
        if plan[key]['tail_visit'] > 0:
            total += 1

    return total


# simulate_movement()
# part1()


# part 2 changes:
plan_v2 = {

}

rope = []


def create_position(row: int, col: int):
    position = f'{row}x{col}'

    plan_v2[position] = {}

    for i, knot in enumerate(rope):
        visit = f'{i}_visit'
        plan_v2[position][visit] = 0


def add_visit_v2(row: int, col: int, index: int):
    position = f'{row}x{col}'

    if not position in plan_v2:
        create_position(row, col)

    visit = f'{index}_visit'
    plan_v2[position][visit] += 1


def init_rope(length: int):

    # adds knots to rope
    for i in range(length):
        rope.append({
            'row': 0,
            'col': 0,
        })

    # creates visits in plan for 0x0
    for i in range(length):
        add_visit_v2(0, 0, i)


def move_v2(direction: DIRECTION):

    for id, knot in enumerate(rope):
        knot_before = rope[id - 1]
        if id == 0:
            head = knot

            match direction:
                case 'U':
                    head['row'] += 1
                case 'D':
                    head['row'] -= 1
                case 'R':
                    head['col'] += 1
                case 'L':
                    head['col'] -= 1

            add_visit_v2(head["row"], head["col"], 0)

        # knot movement is not needed
        elif abs(knot_before['row'] - knot['row']) <= 1 and abs(knot_before['col'] - knot['col']) <= 1:
            continue

        # move
        else:
            'hello'
            if knot_before['row'] > knot['row']:
                knot['row'] += 1

            if knot_before['row'] < knot['row']:
                knot['row'] -=1

            if knot_before['col'] > knot['col']:
                knot['col'] += 1

            if knot_before['col'] < knot['col']:
                knot['col'] -=1

            add_visit_v2(knot["row"], knot["col"], id)

        # moves



def simulate_movement_v2():
    for line in input_v2:
        direction, rept = line.split(' ')
        rept = int(rept)
        for x in range(rept):
            move_v2(direction)


def part2():
    total = 0

    for key in plan_v2.keys():
        # tail visits
        if plan_v2[key][f'{len(rope) - 1}_visit'] > 0:
            total += 1

    return total


init_rope(10)
simulate_movement_v2()
part2()
