input = open("input_3.txt").read()
input_v2 = input.split('\n')
data = list(map(
    lambda row: [
            row[:len(row)//2],
            row[len(row)//2:]
        ]
        ,input_v2
    ))

def char_value(char):
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96  

def find_first_match(str_1, str_2):
    for char in str_1:
        if char in str_2:
            return char

def find_matches(str_1, str_2):
    matches = ''
    for char in str_1:
        if char in str_2:
            matches += char
    return matches

def part_1():
    total = 0
    for row in data:
        total += char_value(find_first_match(row[0],row[1]))

    return total

def part_2():
    total = 0

    for id, row in enumerate(input_v2):
        if (id + 1) % 3 == 0:
           
            total += char_value(
                find_first_match(
                    find_matches(
                        row,
                        input_v2[id-1]
                        ),
                    input_v2[id-2]
                )
            )
    return total


