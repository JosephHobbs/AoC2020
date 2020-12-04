################################################################################
# Advent of Code 2020 - Day 4 - Puzzle 2
################################################################################

import re

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
#
#

hairColorMatcher = re.compile('#[0-9a-z]{6}$')

for passport in passports:
    if all(data in passport for data in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):

        passportHasErrors = False
        fields = passport.split(' ')
        for field in fields:
            if not field:
                continue

            key, value = field.split(':', 2)

            if key == 'byr':
                if not (str(value).isdigit() and 1920 <= int(value) <= 2002):
                    passportHasErrors = True
            elif key == 'iyr':
                if not (str(value).isdigit() and 2010 <= int(value) <= 2020):
                    passportHasErrors = True
            elif key == 'eyr':
                if not (str(value).isdigit() and 2020 <= int(value) <= 2030):
                    passportHasErrors = True
            elif key == 'hgt':
                if 'cm' in str(value):
                    if not (150 <= int(filter(str.isdigit, str(value))) <= 193):
                        passportHasErrors = True
                elif 'in' in str(value):
                    if not (59 <= int(filter(str.isdigit, str(value))) <= 76):
                        passportHasErrors = True
                else:
                    passportHasErrors = True
            elif key == 'hcl':
                if not bool(hairColorMatcher.match(str(value).lower())):
                    passportHasErrors = True
            elif key == 'ecl':
                if not (any(color in str(value) for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])):
                    passportHasErrors = True
            elif key == 'pid':
                if not (str(value).isdigit() and len(value) == 9):
                    passportHasErrors = True

        if not passportHasErrors:
            validPassportCount += 1

print(validPassportCount)

################################################################################
# END
################################################################################
