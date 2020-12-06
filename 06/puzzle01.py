################################################################################
# Advent of Code 2020 - Day 6 - Puzzle 1
################################################################################

possibleAnswers = list('abcdefghijklmnopqrstuvwxyz')

#
#
#

with open('input.txt') as inputFile:
    inputData = inputFile.readlines()

setsOfAnswers = []
currentRecord = ''
for inputRecordRaw in inputData:
    inputRecord = inputRecordRaw.strip()
    if inputRecord == '':
        setsOfAnswers.append(currentRecord.strip())
        currentRecord = ''
        continue

    currentRecord += ' ' + inputRecord

if inputRecord:
    setsOfAnswers.append(currentRecord)

#
#
#

totalYes = 0

for setOfAnswers in setsOfAnswers:
    for possibleAnswer in possibleAnswers:
        if possibleAnswer in setOfAnswers:
            totalYes += 1

print(totalYes)

################################################################################
# END
################################################################################
