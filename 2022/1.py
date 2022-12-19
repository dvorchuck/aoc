

def get_input():
    return open("input_1.txt").read()


def part_one():
    input = get_input()
    bags =  input.split('\n\n')

    max_bag = 0

    for bag in bags:
        numbers = [int(i) for i in bag.split('\n')]
        curr_bag = sum(numbers)
        if curr_bag > max_bag:
            max_bag = curr_bag
    
    answer = max_bag
    print(answer)
    return answer


def part_two():
    input = get_input()
    bags =  input.split('\n\n')

    bags_counted = []

    for bag in bags:
        numbers = [int(i) for i in bag.split('\n')]
        curr_bag = sum(numbers)
        bags_counted.append(curr_bag)
    
    bags_counted.sort()

    top_3 = bags_counted[-3:]

    answer = sum(top_3)
    return answer
