import time

start_time = time.time()
filepath = 'input'

input = "389125467"
# input = 469217538

cups = []
dest = {}
for c in input:
    cupVal = int(c)
    cups.append(cupVal)
    dest[cupVal] = False


valsToMove = []
complete = False

tmpCups = []
while(complete == False):
    for idx in range(9):
        selectedCup = cups[idx]

        for i in range(3):
            tmpCups.append(cups.pop((idx+1) % 9))

        destCup = (selectedCup - 1) % 9
        while destCup in tmpCups:
            destCup = (selectedCup - 1) % 9

        print(destCup)

        # adjIdx = (idx + 4) % 9
        # destination = cups[adjIdx]
        # for i in range(3):
        #     cups.insert((idx + 1) % 9,cups.pop(adjIdx))
        #     movingCups.append(cups.pop)
        # # if dest.get(destination) == True:
        # #     cups.insert((idx + 1) % 9,cups.pop(adjIdx))
        # #     complete = True
        # #     break
        # # else:
        # #     dest[destination] = True
        # #     cups.insert((idx + 1) % 9,cups.pop(adjIdx))

        print(cups)

        if complete == True:
            break



print("--- %s seconds ---" % (time.time() - start_time))