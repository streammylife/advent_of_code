filepath = 'input05'
seats = []

tmpSeatIds = []
tmpSeatId = 0
maxSeatId = 0
missingSeatId = 0

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
    tmpSeatIds.append(tmpSeatId)
    #print(tmpSeatId)
    if tmpSeatId > maxSeatId:
        maxSeatId = tmpSeatId

tmpSearchIds = []
missingIds = []
for i in range(1,127):
    for ii in range (0,8):
        tmpSearchId = i * 8 + ii
        #print(tmpSearchId)
        tmpSearchIds.append(tmpSeatId)
        if tmpSearchId not in tmpSeatIds:
            missingIds.append(tmpSearchId)

for missingId in missingIds:
    if (missingId - 1) in tmpSeatIds:
        if (missingId + 1) in tmpSeatIds:
            print(missingId)

print("tmpSearchIds size: {}".format(len(tmpSearchIds)))
print("tmpSeatIds size: {}".format(len(tmpSeatIds)))


print(missingSeatId)
print(maxSeatId)
