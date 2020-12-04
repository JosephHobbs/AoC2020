################################################################################
# Advent of Code 2020 - Day 4 - Puzzle 1
################################################################################

passports = []
validPassportCount = 0

#
# Read in the input file and preprocess the entries. Our goal is to generate a
# list of passports with attributes all in one line by dropping newlines.
#

with open('0401-input.txt') as inputFile:
    passportsRaw = inputFile.readlines()

currentPassportRaw = ''
for inputLineRaw in passportsRaw:
    inputLine = inputLineRaw.rstrip()
    if not inputLine:
        if currentPassportRaw:
            passports.append(currentPassportRaw)
            currentPassportRaw = ''
    else:
        currentPassportRaw += ' ' + inputLine

if currentPassportRaw:
    passports.append(currentPassportRaw)

#
# Now all we need to do is count the number of passports containing all
# all expected fields.
#

requiredFields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

for passport in passports:
    if all(data in passport for data in requiredFields):
        validPassportCount += 1

print(validPassportCount)

################################################################################
# END
################################################################################
