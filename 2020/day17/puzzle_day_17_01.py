import time
start_time = time.time()

filepath = 'test'

startingGrid = []

coordinates = {}
newCoordinates = {}


def GetCoridinate(x,y,z):
    key = "{},{},{}".format(x,y,z)
    return coordinates.get(key)

def SetCoordinate(x,y,z,val):
    key = "{},{},{}".format(x,y,z)
    coordinates[key] = val

def SetNewCoordinate(x,y,z,val):
    key = "{},{},{}".format(x,y,z)
    newCoordinates[key] = val

def ConvertKeyToXYZ(key):
    tmpCordinate = dict()
    key = key.split(',')
    tmpCordinate['x'] = int(key[0])
    tmpCordinate['y'] = int(key[1])
    tmpCordinate['z'] = int(key[2])
    return tmpCordinate


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   y = 0
   z = 0
   while line:
       line = line.split("\n")[0]
       x = 0
       for c in line:
           SetCoordinate(x,y,z,c)
           x = x + 1

       line = fp.readline()
       y = y + 1

for i in range(6)
    newCoordinates = []
    for key in coordinates.keys():
        tmpCordinate = ConvertKeyToXYZ(key)
        print(tmpCordinate)
        activeNeighbors = 0
        for x in range (tmpCordinate['x']-1,tmpCordinate['x']+1):
            for y in range (tmpCordinate['y']-1,tmpCordinate['y']+1):
                for z in range (tmpCordinate['z']-1,tmpCordinate['z']+1):
                    val = GetCoridinate(x,y,z)
                    if val == '#':
                        activeNeighbors = activeNeighbors + 1
                    elif val == None:
                        SetNewCoordinate(x,y,z,'.')

        
        print(activeNeighbors)


print(coordinates)





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
