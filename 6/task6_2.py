def is_buffer_4_symb_and_diff_chars(buffer):
    if len(buffer) != 14:
        print("wrong buffer size!")
        return False
    if len(buffer) == len(set(buffer)):
        return True

with open('input6_1.txt') as inputfile:
    for line in inputfile:
        total_ctr = 0
        buffer = [] # buffer of 4 - ones we're interested in
        for char in line:
            total_ctr += 1
            
            # only after filling up the first 4, start removing and adding to the buffer of 4.
            # if total_ctr is exactly 4, we know its not a marker since we have the input available
            # and the first 4 characters have a repeating symbol within them (r)
            if total_ctr > 14: 
                buffer.remove(buffer[0]) # remove first element
                buffer.append(char) # add current char to the end
                if is_buffer_4_symb_and_diff_chars(buffer):
                    print("marker found at character number: ")
                    print(total_ctr)
                    print(buffer)
                    break
            else:
                buffer.append(char) # add current char to the end
                
    