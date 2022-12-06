map_2d = []
instructions = []
is_instructions = False

map_2d_ready_to_move = []

def parse_2d_input(map_2d):
    # get total number of columns from the bottom line of the 2d map
    column_numbers_row = map_2d[len(map_2d)-1]
    number_of_columns = int(column_numbers_row[len(column_numbers_row)-2])
    
    # columns will be saved in a dict with the key being the number.
    # I consider this the cleanest way as it allows for change if necessary later
    all_columns = {}
    
    # for each column, create a list that we will use as a stack to represent the column
    for i in range (1,number_of_columns+1):
        all_columns[i] = []
    
    # drop the last line as we no longer need it (the one with 1-2-3-4-5...)
    map_2d.pop()
    # since we want to start from the bottom up, reverse the 2d map list container
    map_2d.reverse()
            
    for line in map_2d:
        for j in range (1,number_of_columns+1):
            first_4 = line[:4]
            if first_4[1] != " ":
                all_columns[j].append(first_4[1])
            line = line[4:]
            
    return all_columns
    
def parse_instruction(instruction):
    instruction = instruction[5:] # remove the word "move" and the space in the beginning
    how_many_we_movin = int(instruction.split(" from ")[0])
    the_rest = instruction.split(" from ")[1]
    source_column = int(the_rest.split(" to ")[0])
    destination_column = int(the_rest.split(" to ")[1])
    
    for i in range(1, how_many_we_movin+1):
        # get value of box and pop it out of the src stack
        box_value = map_2d_ready_to_move[source_column].pop() 
        # append the value of the box to the destination column
        map_2d_ready_to_move[destination_column].append(box_value)

with open('input5_1.txt') as inputfile:
    for line in inputfile:
        if line == "\n":
            is_instructions = True
            continue
        if is_instructions:
            instructions.append(line[0:-1])
        else:
            map_2d.append(line[0:-1])
    # do something with the input now...
    
    map_2d_ready_to_move = parse_2d_input(map_2d)
    
    for instr in instructions:
        parse_instruction(instr)
        
    print(map_2d_ready_to_move)
    
    