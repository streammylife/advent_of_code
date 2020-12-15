import time

filepath = 'input'
data = []

memory = {}
mask = ""
maskOffset = 7

numbers = [8,13,1,0,18,9]
#numbers = [3,1,2]
turn = 1;
turnNumbers = []

prevTurn = {}
prevPrevTurn = {}

lastNum = 0

for num in numbers:
    prevTurn[num] = turn
    turn = turn + 1
    prevPrevTurn[num] = turn
    lastNum = num;


prevTurn.pop(lastNum)

# print("PrevTurn {}".format(prevTurn))
#
# print("------")

while turn < 30000001:
# while turn < 2021:

    # print("------")
    # print("turn {}".format(turn))
    # print("lastNum {}".format(lastNum))
    #print("PrevTurn {}".format(prevTurn))
    # print("prevPrevTurn {}".format(prevPrevTurn))

    prevTurnVal = prevTurn.get(lastNum)
    if(prevTurnVal != None):
        nextNum = turn - prevTurnVal - 1
    else:
        nextNum = 0

    prevTurn[lastNum] = turn - 1

    lastNum = nextNum
    # print("nextNum {}".format(nextNum))

    turn = turn + 1
    # time.sleep(1)
    #print("        ")

print("lastNum {}".format(lastNum))




    #
    # newNum = 0
    #
    # if lastNum in prevPrevTurn.keys():
    #     print("prevTurn {}".format(prevTurn[lastNum]))
    #     newNum = prevTurn[lastNum] - prevPrevTurn[lastNum]
    #     prevPrevTurn[lastNum] = prevTurn[lastNum]
    # else:
    #     prevPrevTurn[lastNum] = prevTurn[lastNum]
    #     newNum = 0
    #
    # lastNum = newNum
    # prevTurn[lastNum] = turn
    # turn = turn + 1
    #
