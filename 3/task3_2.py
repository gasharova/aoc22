all_shared_items = []

def get_shared_type(first, second, third):
    for c in first:
        if c in second:
            if c in third:
                return c
            
def get_priority_for_items(items):
    temp_sum = 0
    for item in items:
        if item.islower():
            temp_sum += ord(item)-96
        else:
            temp_sum += ord(item)-38
    return temp_sum

line_counter = 1
lines = []


with open('input3_2.txt') as inputfile:
    for line in inputfile:
        if line_counter == 4:
            group_item_type = get_shared_type(lines[0], lines[1], lines[2])
            line_counter = 1
            lines.clear()
            all_shared_items += group_item_type

        lines.append(line)
        line_counter += 1
        

total_sum = get_priority_for_items(all_shared_items)
print(total_sum)

