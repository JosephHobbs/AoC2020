################################################################################
# puzzle1.py
################################################################################

#
# Open the input file and store the values in a list
#

with open('input.txt') as fIn:
    reportEntries = fIn.read().splitlines()

#
# For each value, calculate the sister value and see if it's in the list. If
# so, multiply them and return the value.
#

for entry in reportEntries:
    
    currentEntry = int(entry)
    targetValue = 2020 - currentEntry

    if str(targetValue) in reportEntries:
        print("{entry1} * {entry2} = {product}".format(entry1=currentEntry, entry2=targetValue, product=(currentEntry * targetValue)))
        break

################################################################################
# END
################################################################################
