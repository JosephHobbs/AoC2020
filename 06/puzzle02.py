################################################################################
# Advent of Code 2020 - Day 6 - Puzzle 2
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
    setsOfAnswers.append(currentRecord.strip())

#
#
#

totalYes = 0

for setOfAnswers in setsOfAnswers:
    respondentCount = setOfAnswers.count(' ') + 1
    for possibleAnswer in possibleAnswers:
        if setOfAnswers.count(possibleAnswer) == respondentCount:
            totalYes += 1

print(totalYes)

################################################################################
# END
################################################################################
