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


def add_visit(row: int, col:int , type: Literal['head', 'tail']):
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
            
    add_visit(head["row"],head["col"],'head')

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

    add_visit(tail["row"],tail["col"],'tail')



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


simulate_movement()
part1()
