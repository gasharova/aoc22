currentElveCalories = 0
maxCalories1 = 0 #1
maxCalories2 = 0 #2
maxCalories3 = 0 #3

with open('input1_1.txt') as inputfile:
    for l in inputfile:
        if l == "\n":
            if currentElveCalories > maxCalories1:
                maxCalories3 = maxCalories2
                maxCalories2 = maxCalories1
                maxCalories1 = currentElveCalories
                currentElveCalories = 0
                continue
            elif currentElveCalories > maxCalories2:
                maxCalories3 = maxCalories2
                maxCalories2 = currentElveCalories
                currentElveCalories = 0
                continue
            elif currentElveCalories > maxCalories3:
                maxCalories3 = currentElveCalories
                currentElveCalories = 0
            currentElveCalories = 0
            continue
        currentElveCalories = currentElveCalories + int(l)
            
print(maxCalories1 + maxCalories2 + maxCalories3)
print(maxCalories1)
print(maxCalories2)
print(maxCalories3)