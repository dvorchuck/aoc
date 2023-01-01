DAY = 11
input = open(f"input_{DAY}.txt").read()
input_v2 = input.split('\n')


monkeys = []


def init_monkeys():
    # monkey_number: int = None
    monkey_data = None
    for row in input_v2:
        if 'Monkey ' in row:
            monkey_number = int(row.replace('Monkey ', '').replace(':', ''))
            monkey_data = {}
            continue

        if 'Starting items: ' in row:
            starting_items: list = row.replace(
                'Starting items: ', '').strip().split(', ')
            monkey_data['items'] = starting_items
            continue

        if 'Operation: ' in row:
            operation = row.replace('Operation: new = ', '').strip()

            monkey_data['operation'] = operation
            continue

        if 'Test: ' in row:
            test: int = int(row.replace('Test: divisible by ', '').strip())
            monkey_data['test'] = test
            continue

        if 'If true: ' in row:
            target_monkey: int = int(row.replace(
                'If true: throw to monkey ', '').strip())
            monkey_data['throw_true'] = target_monkey
            continue

        if 'If false: ' in row:
            target_monkey: int = int(row.replace(
                'If false: throw to monkey ', '').strip())
            monkey_data['throw_false'] = target_monkey

            monkey_data['items_inspected'] = 0
            monkeys.append(monkey_data)
            continue


init_monkeys()


def throw(monkey):
    for item in monkey['items']:
        worry_level = eval(monkey['operation'].replace('old', str(item))) // 3

        if worry_level % monkey['test'] == 0:
            monkeys[monkey['throw_true']]['items'].append(worry_level)
        else:
            monkeys[monkey['throw_false']]['items'].append(worry_level)

        monkey['items_inspected'] += 1

    monkey['items'] = []


def throw_round():

    for monkey in monkeys:
        throw(monkey)


def part1():
    for _ in range(20):
        throw_round()

    totals = []
    for monkey in monkeys:
        totals.append(monkey['items_inspected'])

    totals.sort()
    max1, max2 = totals[-2:]
    return max1 * max2

# part 2


def calculate_divisor():
    divisor = 1

    for monkey in monkeys:
        divisor *= monkey['test']

    return divisor


common_divisor = calculate_divisor()


def throw_v2(monkey):
    for item in monkey['items']:
        worry_level = eval(monkey['operation'].replace(
            'old', str(item))) % common_divisor

        if worry_level % monkey['test'] == 0:
            monkeys[monkey['throw_true']]['items'].append(worry_level)
        else:
            monkeys[monkey['throw_false']]['items'].append(worry_level)

        monkey['items_inspected'] += 1

    monkey['items'] = []


def throw_round_v2():

    for monkey in monkeys:
        throw_v2(monkey)


def part2():
    for _ in range(10000):
        throw_round_v2()

    totals = []
    for monkey in monkeys:
        totals.append(monkey['items_inspected'])

    totals.sort()
    max1, max2 = totals[-2:]
    return max1 * max2


part2()

'''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
'''
''
