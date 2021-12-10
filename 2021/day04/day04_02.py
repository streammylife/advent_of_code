import time

start_time = time.time()


drawingNums = []

filepath = 'input_drawing'
with open(filepath) as fp:
   line = fp.readline()
   drawingNums = line.split(',')

boards = []

filepath = 'input'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   board = []
   while line:
       line = line.strip('\n')
       if len(line) > 0:
           for num in line.split(' '):
               if num != '':
                   board.append(num)
       else:
           boards.append(board)
           board = []
       line = fp.readline()

colResults = {}
rowResults = {}


done = False

winningBoards = []

for ii in range(len(drawingNums)):
    num = drawingNums[ii]
    for i in range(len(boards)):
        if i not in winningBoards:
            board = boards[i]
            if num in board:
                idx = board.index(num)
                col = idx % 5
                row = idx / 5
                keyRow = str(i) + ',' + str(row)
                keyCol = str(i) + ',' + str(col)

                #board.remove(num)

                if keyCol in colResults.keys():
                    colResults[keyCol] = colResults[keyCol] + 1
                else:
                    colResults[keyCol] = 1
                if colResults[keyCol] >= 5:
                    if i not in winningBoards:
                        winningBoards.append(i)

                if keyRow in rowResults.keys():
                    rowResults[keyRow] = rowResults[keyRow] + 1
                else:
                    rowResults[keyRow] = 1
                if rowResults[keyRow] >= 5:
                    if i not in winningBoards:
                        winningBoards.append(i)
    if len(boards) == len(winningBoards):
        break

lastWinningBoard =  boards[winningBoards[len(winningBoards)-1]]
drawingNums = drawingNums[:ii+1]
sum = 0
for dig in lastWinningBoard:
    if dig not in drawingNums:
        sum = sum + int(dig)
res = sum * int(num)
print("done")


#21070 is too high
#17836 is too high

print("--- %s seconds ---" % (time.time() - start_time))