my_score = 0
letter_to_move = {'A': 'rock', 'B': 'pap', 'C': 'sci'}
letter_to_match_result = {'X': 'loss', 'Y': 'draw', 'Z': 'win'}

def get_my_move(their_move, result):
    if result == 'draw':
        return their_move
        
    if their_move == 'rock':
        if result == 'win':
            return 'pap'
        else:
            return 'sci'
            
    if their_move == 'pap':
        if result == 'win':
            return 'sci'
        else:
            return 'rock'
    
    if result == 'win':
        return 'rock'
    return 'pap'

def calculate_match_points(match_result):
    if match_result == 'win':
        return 6
    elif match_result == 'loss':
        return 0
    else:
        return 3

def calculate_bonus_points(move):
    if move == 'rock':
        return 1
    elif move == 'pap':
        return 2
    else:
        return 3 #scissors

my_points = 0

with open('input2_1.txt') as inputfile:
    for line in inputfile:
        their_move = letter_to_move[line[0]]
        result = letter_to_match_result[line[2]]
            
        my_move = get_my_move(their_move, result)
        
        match_points_for_me = calculate_match_points(result)
        bonus_points_for_me = calculate_bonus_points(my_move)
        my_points = my_points + match_points_for_me + bonus_points_for_me
        
print(my_points)