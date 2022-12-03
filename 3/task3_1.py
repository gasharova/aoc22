all_shared_items = []

def get_shared_types_list(first, second):
    for c in first:
        if c in second:
            return c
            
def get_priority_for_items(items):
    temp_sum = 0
    for item in items:
        if item.islower():
            #print(item + ' ' + str(ord(item)-96) + '\n')
            temp_sum += ord(item)-96
        else:
            #print(item + ' ' + str(ord(item)-38) + '\n')
            temp_sum += ord(item)-38
    return temp_sum

with open('input3_1.txt') as inputfile:
    for line in inputfile:
        compartment_size = int(len(line)/2)
        #print(line)
        first_compartment = line[0:compartment_size]
        second_compartment = line[compartment_size:len(line)-1]
        #print(first_compartment)
        #print(second_compartment)
        shared_item = get_shared_types_list(first_compartment, second_compartment)
        #print(shared_item)
        all_shared_items += shared_item
        
#all_shared_items_unique = list(dict.fromkeys(all_shared_items))
total_sum = get_priority_for_items(all_shared_items)
print(total_sum)