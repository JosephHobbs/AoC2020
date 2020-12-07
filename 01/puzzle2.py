################################################################################
# puzzle2.py
################################################################################

reportEntries = [int(i) for i in open('input.txt').readlines() if i]

for first in reportEntries:
    for second in reportEntries:
        for third in reportEntries:
            if first + second + third == 2020:
                print(first * second * third)

################################################################################
# END
################################################################################
