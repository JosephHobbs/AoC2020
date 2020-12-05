################################################################################
# Advent of Code 2020 - Day 5 - Puzzle 2
################################################################################

seats = []

with open('input.txt') as inputFile:
    seatsEncoded = inputFile.readlines()

for seatEncodedRaw in seatsEncoded:

    rowData = seatEncodedRaw.strip()[0:7]
    row = int(rowData.replace('B', '1').replace('F', '0'), 2)

    seatData = seatEncodedRaw.strip()[7:10]
    seat = int(seatData.replace('R', '1').replace('L', '0'), 2)

    seats.append(row * 8 + seat)

seats.sort()
mySeatId = seats[0] - 1
for possibleSeatId in seats:
    mySeatId += 1
    if mySeatId != possibleSeatId:
        break

print(mySeatId)

################################################################################
# END
################################################################################
