import time

filepath = 'input'
rows = []
marginHigh = 3

# windowLen = 25
# invalidNum = 57195069

rowWidth = 0

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.split("\n")
       tmpRow = []
       for c in line[0]:
           tmpRow.append(c)
       rows.append(tmpRow)
       line = fp.readline()


complete = False
newRows = []
rowWidth = len(rows[0])
numOfRows = len(rows)
while complete == False:
    # print("-------------------------")
    # print(rows)
    complete = True
    newRows = []
    for i in range(len(rows)):
        tmpRow = []
        for ii in range(len(rows[i])):
            if(rows[i][ii] ==  'L'):
                doUpdate = True
                for x in range(3):
                    for y in range(3):
                        tmpX = (i - 1 + x)
                        tmpY = (ii - 1 + y)
                        if(tmpX > -1 and tmpX <numOfRows and tmpY > -1 and tmpY < rowWidth):
                            if(rows[tmpX][tmpY] == '#'):
                                doUpdate = False
                if(doUpdate):
                    tmpRow.append('#')
                    complete = False
                else:
                    tmpRow.append('L')
            elif(rows[i][ii] ==  '#'):
                occCnt = 0
                for x in range(3):
                    for y in range(3):
                        tmpX = (i - 1 + x)
                        tmpY = (ii - 1 + y)
                        if(tmpX > -1 and tmpX <numOfRows and tmpY > -1 and tmpY < rowWidth):
                            tmpChar = rows[tmpX][tmpY]
                            if(tmpChar == '#'):
                                occCnt = occCnt + 1
                occCnt = occCnt - 1
                if(occCnt > 3):
                    tmpRow.append('L')
                    # print("updating #")
                    complete = False
                else:
                    tmpRow.append('#')
            else:
                tmpRow.append('.')
        newRows.append(tmpRow)
    rows = newRows
    #time.sleep(2)

occCnt = 0
for r in rows:
    for s in r:
        if s == '#':
            occCnt = occCnt + 1

print(occCnt)
