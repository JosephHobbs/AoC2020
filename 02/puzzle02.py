################################################################################
# Advent of Code 2020 - Day 2 - Puzzle 2
################################################################################

with open('input.txt') as inputFile:
    inputData = inputFile.readlines()

validPasswords = 0

for inputLine in inputData:

    if not inputLine:
        continue

    (targetFields, targetCharRaw, password) = inputLine.rstrip().split(' ', 3)
    (targetField1, targetField2) = str(targetFields).split('-', 2)
    targetChar = str(targetCharRaw)[0]

    field1Char = str(password)[int(targetField1) - 1]
    field2Char = str(password)[int(targetField2) - 1]

    if (field1Char == targetChar or field2Char == targetChar) and (field1Char != field2Char):
        validPasswords += 1

print(validPasswords)

################################################################################
# END
################################################################################
