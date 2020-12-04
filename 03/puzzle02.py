################################################################################
# Advent of Code 2020 - Day 3 - Puzzle 2
################################################################################

xChange = [1, 3, 5, 7, 1]
yChange = [1, 1, 1, 1, 2]

with open('input.txt') as inputFile:
    inputData = inputFile.readlines()

rows = []
for inputLine in inputData:
    if inputLine:
        rows.append(list(inputLine.strip()))

scenarioTotals = []

for scenario in range(0, len(xChange)):

    treeCount = 0
    positionX = 0
    positionY = 0

    while True:

        positionX += xChange[scenario]
        positionY += yChange[scenario]

        if positionY >= len(rows):
            break

        currentRowWidth = len(rows[positionY])

        if positionX >= currentRowWidth:
            positionX -= currentRowWidth

        if rows[positionY][positionX] == '#':
            treeCount += 1

    scenarioTotals.append(treeCount)

finalResult = 1
for scenario in scenarioTotals:
    finalResult *= scenario

print(finalResult)

################################################################################
# END
################################################################################
