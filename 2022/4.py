input = open("input_4.txt").read()
input_v2 = input.split('\n')

data = []

for row in input_v2:
    ranges = row.split(',')

    row_data = []
    for range in ranges:
        numbers = range.split('-')
        
        for number in numbers:
            row_data.append(int(number))


    data.append(row_data)

def ranges_match(row):
    start_1, end_1, start_2, end_2 = row
    if start_1 >= start_2 and start_1 <= end_2 and end_1 >= start_2 and end_1 <= end_2:
        return 1
    elif start_2 >= start_1 and start_2 <= end_1 and end_2 >= start_1 and end_2 <= end_1:
        return 1
    else: 
        return 0

def ranges_cross(row):
    start_1, end_1, start_2, end_2 = row
    if (start_1 >= start_2 and start_1 <= end_2) or (end_1 >= start_2 and end_1 <= end_2):
        return 1
    elif (start_2 >= start_1 and start_2 <= end_1) or (end_2 >= start_1 and end_2 <= end_1):
        return 1
    else: 
        return 0

def part_1():
    total = 0
    for row in data:
        total += ranges_match(row)
    return total


def part_2():
    total = 0
    for row in data:
        total += ranges_cross(row)
    return total

