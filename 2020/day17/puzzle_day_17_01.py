import time
start_time = time.time()

filepath = 'test'

startingGrid = []

x = 0
y = 0
z = 0


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.split("\n")[0]
       row = []
       for c in line:
           row.append(c)
       startingGrid.append(row)

       line = fp.readline()

print(startingGrid)



print("--- %s seconds ---" % (time.time() - start_time))




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
