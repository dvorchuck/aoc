input = open("input_5.txt").read()
input_v2 = input.split('\n')

input_moves = []
input_crates = []

orders = []
crates = []

for row in input_v2:

    # useless rows
    
    if len(row) == 0:
        continue
    #move orders
    elif row[0] == 'm':
        input_moves.append(row)

    elif  '[' not in row:
        continue

    # boxes
    else:
        input_crates.append(row)

# cleaning orders
for row in input_moves:
    clean = row.replace('move ','').replace('from ','').replace('to ','').split(' ')
    order = []

    for e in clean:
        order.append(int(e))

    orders.append(order)


# cleaning crates
number_of_columns = (len(input_crates[0]) + 1) // 4

for _ in range(number_of_columns):
    crates.append([])


for row in reversed(input_crates):
    for id,char in enumerate(row):
        if (id + 2) % 4 == 0 and not row[id] == ' ':
            
            crates[(id + 1) // 4].append(row[id - 1])


# print(input_moves)
# print(input_crates)
# print(orders)
print(crates)


def move(order):
    iteration, source, target = order

    for _ in range(iteration):
        crates[target - 1].append(
            crates[source - 1].pop()
        )

def better_move(order):
    iteration, source, target = order

    moved = crates[source - 1][-iteration:]
    del crates[source - 1][-iteration:]
    crates[target - 1].extend(moved)


def part1():
    result = ''
    for order in orders:
        move(order)

    for column in crates:
        
        result += str(column[-1])

    return result
    
def part2():
    result = ''
    for order in orders:
        better_move(order)

    for column in crates:
        
        result += str(column[-1])

    return result
