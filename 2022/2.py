
input = open("input_2.txt").read()


win_dict = {
    'A':'Y',  #rock
    'B':'Z',   #paper
    'C':'X'    #scissors
}

equal_dict = {
    'A':'X',  #rock
    'B':'Y',   #paper
    'C':'Z'    #scissors
}



scores = {
    'X': 1,  #rock
    'Y': 2,   #paper
    'Z': 3,    #scissors
    'A': 1,  #rock
    'B': 2,   #paper
    'C': 3,    #scissors
}


def calculate_outcome_1(round):
    choices = round.split(' ')
    if win_dict[choices[0]] == choices[1]:
        return 6
    elif equal_dict[choices[0]] == choices[1]:
        return 3
    else:
        return 0

def calculate_outcome_2(round):
    choices = round.split(' ')

    score = {
        'X':0,
        'Y':3,
        'Z':6
    }
    return score[choices[1]]


def calculate_shape_score_2(round):
    choices = round.split(' ')
    score = 0
    if(choices[1] == 'Y'):
        score = scores[choices[0]]
    elif(choices[1] == 'Z'):
        score = scores[choices[0]] + 1
    else:
        score = scores[choices[0]] - 1

    
    if(score == 4):
        score = 1

    if(score == 0):
        score = 3
    return score

def part_one():
    rows = input.split('\n')
    
    total = 0

    for row in rows:
        total += calculate_outcome_1(row)
        total += scores[row.split(' ')[1]]

    answer = total
    return answer

# print(part_one())

def part_two():
    rows = input.split('\n')
    
    total = 0

    for row in rows:
        total += calculate_outcome_2(row)
        total += calculate_shape_score_2(row)

    answer = total
    return answer

