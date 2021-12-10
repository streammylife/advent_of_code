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

for ii in range(len(drawingNums)):
    num = drawingNums[ii]
    for i in range(len(boards)):
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
                done = True
                break

            if keyRow in rowResults.keys():
                rowResults[keyRow] = rowResults[keyRow] + 1
            else:
                rowResults[keyRow] = 1
            if rowResults[keyRow] >= 5:
                done = True
                break

    if done:
        break

drawingNums = drawingNums[:ii+1]
sum = 0
for dig in board:
    if dig not in drawingNums:
        sum = sum + int(dig)
res = sum * int(num)
print("done")


#106821 is too high

print("--- %s seconds ---" % (time.time() - start_time))