currentElveCalories = 0
maxCalories = 0

with open('input1_1.txt') as inputfile:
    for l in inputfile:
        if l == "\n":
            currentElveCalories = 0
            continue
        currentElveCalories = currentElveCalories + int(l)
        if currentElveCalories > maxCalories:
            maxCalories = currentElveCalories
            
print(maxCalories)