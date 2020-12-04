################################################################################
# Advent of Code 2020 - Day 3 - Puzzle 1
################################################################################

xChange = 3
yChange = 1

with open('input.txt') as inputFile:
    inputData = inputFile.readlines()

rows = []
for inputLine in inputData:
    if inputLine:
        rows.append(list(inputLine.strip()))

treeCount = 0
positionX = 0
positionY = 0

while True:

    positionX += xChange
    positionY += yChange

    if positionY >= len(rows):
        break

    currentRowWidth = len(rows[positionY])

    if positionX >= currentRowWidth:
        positionX -= currentRowWidth

    if rows[positionY][positionX] == '#':
        treeCount += 1

print(treeCount)

################################################################################
# END
################################################################################
