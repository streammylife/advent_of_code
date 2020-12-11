import time

filepath = 'input'
rows = []
marginHigh = 3

# windowLen = 25
# invalidNum = 57195069

rowWidth = 0

def FindFirstSeatInDir(rowsToSearch, pos, dir):
    slope = [0,0]

    returnVal = 'N'

    maxX = len(rowsToSearch[0]) - 1
    maxY = len(rowsToSearch) - 1

    if dir == 0: #west
        slope = [-1,0]
    elif dir == 1: #northwest
        slope = [-1,-1]
    elif dir == 2: #north
        slope = [0,-1]
    elif dir == 3: #northeast
        slope = [1,-1]
    elif dir == 4: #east
        slope = [1,0]
    elif dir == 5: #southeast
        slope = [1,1]
    elif dir == 6: #south
        slope = [0,1]
    elif dir == 7: #southwest
        slope = [-1,1]

    searchEnd = False
    x = pos[0]
    slopeX = slope[0]
    y = pos[1]
    slopeY = slope[1]
    while(searchEnd == False):
        x = x + slopeX
        y = y + slopeY

        if(x < 0 or x > maxX or y < 0 or y > maxY): #outside edge of grid
            searchEnd = True
        else:
            seat = rowsToSearch[y][x]
            if seat != '.':
                returnVal = seat;
                searchEnd = True

    return returnVal

newRows = []

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
while complete == False:
    complete = True
    newRows = []
    for i in range(len(rows)):
        tmpRow = []
        for ii in range(len(rows[i])):
            seatEval = []
            seat = rows[i][ii]
            # print(seat)
            if seat != '.':
                pos = [ii, i]
                seatEval = []
                for dir in range(8):
                    seatEval.append(FindFirstSeatInDir(rows, pos, dir))

                #print(seatEval)
                if seat == '#':
                    if(seatEval.count('#') > 4):
                        tmpRow.append('L')
                        complete = False
                    else:
                        tmpRow.append(seat)
                elif seat == 'L':
                    if(seatEval.count('#') == 0):
                        tmpRow.append('#')
                        complete = False
                    else:
                        tmpRow.append(seat)
                # else:
                #     tmpRow.append(seat)
            else:
                tmpRow.append('.')
        newRows.append(tmpRow)
    rows = newRows

count = 0
for row in newRows:
    count = count + row.count('#')

print(count)

        # print(seatEval)
