filepath = 'input05'
seats = []

tmpSeatId = 0
maxSeatId = 0

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       seats.append(line)
       line = fp.readline()

for seat in seats:
    rowPos = 0;
    rowVal = 128;
    for x in range(7):
        rowVal /= 2
        if(seat[x] == 'B'):
            rowPos += rowVal
        #print(rowPos)

    colPos = 0;
    colVal = 8;
    for x in range(7,10):
        colVal /= 2
        if(seat[x] == 'R'):
            colPos += colVal
        #print(colPos)

    tmpSeatId = rowPos * 8 + colPos
    #print(tmpSeatId)
    if tmpSeatId > maxSeatId:
        maxSeatId = tmpSeatId

print(maxSeatId)
