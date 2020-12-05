################################################################################
# Advent of Code 2020 - Day 5 - Puzzle 1
################################################################################

seats = []

with open('input.txt') as inputFile:
    seatsEncoded = inputFile.readlines()

for seatEncodedRaw in seatsEncoded:

    rowData = seatEncodedRaw.strip()[0:7]
    row = int(rowData.replace('B', '1').replace('F', '0'), 2)

    seatData = seatEncodedRaw.strip()[7:10]
    seat = int(seatData.replace('R', '1').replace('L', '0'), 2)

    seats.append([row, seat, (row * 8 + seat)])

highestSeatId = 0
for currentSeat in seats:
    if int(currentSeat[2]) > highestSeatId:
        highestSeatId = int(currentSeat[2])

print(highestSeatId)

################################################################################
# END
################################################################################
