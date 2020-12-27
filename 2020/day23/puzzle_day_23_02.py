import time

start_time = time.time()
filepath = 'input'

input = "389125467"
# input = "469217538"

cups = []
dest = {}
for c in input:
    cupVal = int(c)
    cups.append(cupVal)
    # dest[cupVal] = False

startVal = 10
while len(cups) < 1000000:
    cups.append(startVal)
    # dest[startVal] = False
    startVal = startVal + 1


valsToMove = []
complete = False

tmpCups = []
i = 0

completePerc = 10

numOfCups = len(cups)

numberOfRounds = 10000000

nextSelectionIdx = 0

for i in range(numberOfRounds):
    selectedCup = cups[nextSelectionIdx]

    timeTracker = time.time()
    # if (i + 1) % 1000:
    #     print i
    # print(cups)
    # print("sel cup: {}".format(selectedCup))

    tmpCups = []

    idxToPop = nextSelectionIdx + 1

    for ii in range(3):
        if idxToPop > (len(cups) - 1):
            idxToPop = 0
        tmpCups.append(cups.pop(idxToPop))




    destCup = selectedCup - 1
    if destCup < 1:
        destCup = numOfCups

    while destCup in tmpCups:
        destCup = destCup - 1
        if destCup < 1:
            destCup = numOfCups

    # print("dest cup: {}".format(destCup))

    destIdx = cups.index(destCup)


    for ii in range(3):
        cups.insert(destIdx + ii + 1,tmpCups[ii])


    nextSelectionIdx = (cups.index(selectedCup) + 1) % len(cups)

    print("--- %s seconds ---" % (time.time() - timeTracker))




# while(i < 10):
# #while(i < 10000000):
#
#     for i in range()
#
#     selectedCup = cups[0]
#     tmpCups = cups[1:4]
#     cups = cups[0:1] + cups[4:]
#
#     destCup = selectedCup - 1
#     if destCup < 1:
#         destCup = 9
#
#     while destCup in tmpCups:
#         destCup = destCup - 1
#         if destCup < 1:
#             destCup = 9
#
#     # if dest.get(destCup) == True:
#     #     complete = True
#
#     dest[destCup] = True
#
#     destIdx = cups.index(destCup)
#
#     cups = cups[:destIdx+1] + tmpCups + cups[destIdx+1:]
#     cups = cups[1:] + cups[0:1]
#
#     i = i + 1
#
#     # print(cups)
#
#
#     # for idx in range(9):
#         # selectedCup = cups[idx]
#         #
#         # for i in range(3):
#         #     tmpCups.append(cups.pop((idx+1) % 9))
#         #
#         # destCup = (selectedCup - 1) % 9
#         # while destCup in tmpCups:
#         #     destCup = (selectedCup - 1) % 9
#         #
#         # print(destCup)
#         #
#         # # adjIdx = (idx + 4) % 9
#         # # destination = cups[adjIdx]
#         # # for i in range(3):
#         # #     cups.insert((idx + 1) % 9,cups.pop(adjIdx))
#         # #     movingCups.append(cups.pop)
#         # # # if dest.get(destination) == True:
#         # # #     cups.insert((idx + 1) % 9,cups.pop(adjIdx))
#         # # #     complete = True
#         # # #     break
#         # # # else:
#         # # #     dest[destination] = True
#         # # #     cups.insert((idx + 1) % 9,cups.pop(adjIdx))
#         #
#         # print(cups)
#         #
#         # if complete == True:
#         #     break
#
#
findIdx = cups.index(1)
val1 = cups[findIdx + 1]
val2 = cups[findIdx + 2]
valM = val1 * val2

print(valM)

# print(cups)

print("--- %s seconds ---" % (time.time() - start_time))