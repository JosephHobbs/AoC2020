################################################################################
# Advent of Code 2020 - Day 2 - Puzzle 1
################################################################################

with open('input.txt') as inputFile:
    inputData = inputFile.readlines()

validPasswords = 0

for inputLine in inputData:

    if not inputLine:
        continue

    (targetCount, targetCharRaw, password) = inputLine.rstrip().split(' ', 3)
    (targetCountMin, targetCountMax) = str(targetCount).split('-', 2)
    targetChar = str(targetCharRaw)[0]

    if int(targetCountMin) <= str(password).count(targetChar) <= int(targetCountMax):
        validPasswords += 1

print(validPasswords)

################################################################################
# END
################################################################################
