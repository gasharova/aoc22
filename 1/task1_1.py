currentElveNum = 1 #first
currentElveCalories = 0

maxCaloriesElveNum = 0
maxCalories = 0

with open('input1_1.txt') as inputfile:
    for l in inputfile:
        if l == "\n":
            currentElveCalories = 0
            currentElveNum += 1
            continue
        currentElveCalories = currentElveCalories + int(l)
        if currentElveCalories > maxCalories:
            maxCalories = currentElveCalories
            
print(maxCalories)