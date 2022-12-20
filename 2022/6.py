input = open("input_6.txt").read()


def part_2():
    for id, char in enumerate(input):
        string = input[id:id+4]

        is_start = True

        for letter in string:
            is_start = True
            test_string = string.replace(letter, '')
            if len(test_string) < 3:
                is_start = False
                break

        if is_start:
            return id + 4


def part_2():
    for id, char in enumerate(input):
        string = input[id:id+14]

        is_start = True

        for letter in string:
            is_start = True
            test_string = string.replace(letter, '')
            if len(test_string) < 13:
                is_start = False
                break

        if is_start:
            return id + 14


