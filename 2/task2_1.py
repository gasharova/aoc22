my_score = 0
letter_to_move = {'A': 'rock', 'B': 'pap', 'C': 'sci', 'X': 'rock', 'Y': 'pap', 'Z': 'sci'}

def match_result(their_move, my_move):
    if my_move == their_move:
        return 'draw'
        
    if my_move == 'rock':
        if their_move == 'sci':
            return 'win'
        else:
            return 'loss'
        
    if my_move == 'sci':
        if their_move == 'pap':
            return 'win'
        else:
            return 'loss'
        
    if their_move == 'rock': # my move must be paper at this point and they must have a different move
        return 'win'
    else:
        return 'loss' 

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
        my_move = letter_to_move[line[2]]
            
        print(my_move + ' ' + str(calculate_bonus_points(my_move)))
        print('\n')
        match_points_for_me = calculate_match_points(match_result(their_move, my_move))
        bonus_points_for_me = calculate_bonus_points(my_move)
        my_points = my_points + match_points_for_me + bonus_points_for_me
        
print(my_points)