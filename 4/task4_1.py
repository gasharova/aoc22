def does_first_fully_contain_second(list1, list2):
    for item in list2:
        if item not in list1:
            return False
    return True
        
def does_any_contain_the_other(l1, l2):
    return does_first_fully_contain_second(l1,l2) or does_first_fully_contain_second(l2,l1)
    
def parse_range(range_string):
    lower_range = range_string.split("-")[0]
    upper_range = range_string.split("-")[1]
    lower_range = int(lower_range)
    upper_range = int(upper_range)
    
    if lower_range == upper_range:
        singleitem_list = []
        singleitem_list.append(lower_range)
        return singleitem_list
    
    return list(range(lower_range, upper_range+1))

counter = 0

with open('input4_1.txt') as inputfile:
    for line in inputfile:
        first_elve = line.split(",")[0]
        second_elve = line.split(",")[1]
        
        first_elve = parse_range(first_elve)
        second_elve = parse_range(second_elve)
        
        if does_any_contain_the_other(first_elve, second_elve):
            counter += 1
            
print(counter)