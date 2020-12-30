import time
import copy

start_time = time.time()

tiles = {}

edgeMatches = {"top": "bottom", "right": "left", "bottom": "top", "left": "right"}

def rotateTile(tmpTileId, tmpTiles):
    tmpTile = tmpTiles.get(tmpTileId)
    edgeList = ["top", "right", "bottom", "left"]

    for edge in edgeList:
        tmpEdge = tmpTile.get(edge)
        tmpEdge[0] = (tmpEdge[0] - 1) % 4

def flipTileX(tmpTileId, tmpTiles):
    tmpTile = tmpTiles.get(tmpTileId)
    tmpEdge = tmpTile.get("left")[:]
    tmpTile.get("left")[0] = tmpTile.get("right")[0]
    tmpTile.get("right")[0] = tmpEdge[0]
    tmpEdges = tmpTile.get("edges")

    for i in range(len(tmpEdges)):
        tmpEdges[i] = tmpEdges[i][::-1]

def rotateGrid(g1):

    gridSize = (sorted(g1.keys(),reverse=True)[0][0]) + 1

    newTileGrid = {}
    for key in g1.keys():
        newKey = (gridSize - 1 - key[1], key[0])
        newTileGrid[newKey] = copy.deepcopy(g1[key])
    return newTileGrid

def flipGrid(g1):

    gridSize = (sorted(g1.keys(),reverse=True)[0][0]) + 1

    newTileGrid = {}
    for key in g1.keys():
        newKey = (gridSize - 1 - key[0], key[1])
        newTileGrid[newKey] = copy.deepcopy(g1[key])
    return newTileGrid

def reorientGrid(tmpTileId, tmpTiles, searchRnd):
    """

    :type tmpTiles: object
    """
    tmpTileGrid = tmpTiles.get(tmpTileId).get("grid")
    newTileGrid = copy.deepcopy(tmpTileGrid)

    if searchRnd > 3:
        #gotta flip it
        newTileGrid = flipGrid(newTileGrid)
        rotations = searchRnd - 4
    else:
        rotations = searchRnd

    for i in range(rotations):
        newTileGrid = rotateGrid(newTileGrid)

    tmpTiles.get(tmpTileId)["grid"] = copy.deepcopy(newTileGrid)





filepath = 'input'
initialCount = 0
with open(filepath) as fp:
    line = fp.readline()
    tile = {}
    grid = {}
    tileIdFound = False
    tileLine = 0
    tileId = ""
    top = ""
    right = ""
    bottom = ""
    left = ""

    while line:

        if line.isspace():
            tileIdFound = False

            # reverse bottom and left strings to keep order clockwise
            bottom = bottom[::-1]
            left = left[::-1]

            tile["edges"] = [top, right, bottom, left]

            tile["top"] = [0, False, ""]
            tile["right"] = [1, False, ""]
            tile["bottom"] = [2, False, ""]
            tile["left"] = [3, False, ""]

            tile["grid"] = copy.deepcopy(grid)

            tiles[tileId] = tile.copy()
            tile = {}
            tileId = ""
            top = ""
            right = ""
            bottom = ""
            left = ""
            tileLine = 0

            grid ={}

        else:
            if not tileIdFound:
                tileId = line.split()[1].split(':')[0]
                tileIdFound = True
            else:
                line = line.split('\n')[0]
                tileLen = len(line)

                # store all the vals in clockwise order
                for i in range(tileLen):
                    lineEntry = line[i]

                    if lineEntry == '#':
                        initialCount = initialCount + 1

                    if i > 0 and i < (tileLen - 1):
                        if tileLine > 0 and tileLine <(tileLen - 1):
                            grid[(i-1,tileLine-1)] = lineEntry

                    # add top line
                    if tileLine == 0:
                        top = top + lineEntry

                    # add right line
                    if i == (tileLen - 1):
                        right = right + lineEntry

                    # add bottom line
                    if tileLine == (tileLen - 1):
                        bottom = bottom + lineEntry

                    # add left line
                    if i == 0:
                        left = left + lineEntry

                tileLine = tileLine + 1

        line = fp.readline()

filepath = 'monster'
monster = {}
with open(filepath) as fp:
    line = fp.readline()
    lineNum = 0
    while line:
        line = line.split('\n')[0]
        for i in range(len(line)):
            if line[i] == '.':
                c = " "
            else:
                c = line[i]
            monster[(i,lineNum)] = c
        lineNum = lineNum + 1
        line = fp.readline()

#pick an arbitrary tile to start with
key = tiles.keys()[0]

# #test rotate and copy
# rotateTile(key, tiles)
# rotateTile(key, tiles)
# rotateTile(key, tiles)
# rotateTile(key, tiles)
# refTile = copy.deepcopy(tiles.get(key))
# flipTileX(key, tiles)
# flipTileX(key, tiles)


foundPieces = {key: tiles.pop(key)}

complete = False
newFoundPieces = {}
while not complete:
    complete = True
    for key1 in tiles.keys():
        # print("Key1: {}".format(key1))
        loosePiece = tiles.get(key1)

        matchFound = False
        searchRound = 0
        while not matchFound and searchRound < 8:
            for edgeKey in edgeMatches.keys():
                looseEdge = loosePiece.get(edgeKey)
                if not looseEdge[1]:
                    for key2 in foundPieces.keys():
                        # print("------Key2: {}".format(key2))
                        foundPiece = foundPieces.get(key2)
                        matchEdge = edgeMatches.get(edgeKey)
                        foundEdge = foundPiece.get(matchEdge)
                        if not foundEdge[1]:
                            e1 = foundPiece.get("edges")[foundEdge[0]]
                            e2 = loosePiece.get("edges")[looseEdge[0]][::-1]
                            if e1 == e2:
                                foundEdge[1] = True
                                foundEdge[2] = key1
                                looseEdge[1] = True
                                looseEdge[2] = key2
                                newFoundPieces[key1] = loosePiece
                                matchFound = True

            if not matchFound:
                if key1 == "3079":
                    print("shit before anything")
                    for i in range(8):
                        line = ""
                        for ii in range(8):
                            line = line + tiles.get("3079").get("grid").get((ii,i))
                        print(line)
                # grid = tiles.get(key1).get("grid")
                rotateTile(key1, tiles)
                tiles[key1]["grid"] = rotateGrid(tiles[key1]["grid"]).copy()
                if searchRound == 3:
                    flipTileX(key1,tiles)
                    # grid = tiles.get(key1).get("grid")
                    tiles[key1]["grid"] = flipGrid(tiles[key1]["grid"]).copy()
                    if key1 == "3079":
                        tiles[key1]["grid"] = rotateGrid(tiles[key1]["grid"]).copy()
                        tiles[key1]["grid"] = rotateGrid(tiles[key1]["grid"]).copy()
                        # tiles.get(key1)["grid"] = rotateGrid(grid)
                        # tiles.get(key1)["grid"] = rotateGrid(grid)
                        # tiles.get(key1)["grid"] = rotateGrid(grid)
                        print("shit after flip and weird shit")
                        for i in range(8):
                            line = ""
                            for ii in range(8):
                                line = line + tiles.get("3079").get("grid").get((ii, i))
                            print(line)
                searchRound = searchRound + 1
            else:
                if key1 == "3079":
                    print("shit")
                    for i in range(8):
                        line = ""
                        for ii in range(8):
                            line = line + tiles.get("3079").get("grid").get((ii,i))
                        print(line)

        if len(newFoundPieces) > 0:
            complete = False
            foundPieces.update(newFoundPieces)
            for key in newFoundPieces.keys():
                tiles.pop(key)
            newFoundPieces = {}

corners = []

for key in foundPieces.keys():
    edgeList = ["top", "right", "bottom", "left"]
    edgeMatchCount = 0
    for edge in edgeList:
        if foundPieces.get(key).get(edge)[1]:
            edgeMatchCount = edgeMatchCount + 1

    if edgeMatchCount == 2:
        corners.append(key)



prod = 1
topLeft = ""
for corner in corners:
    prod = prod * int(corner)
    if foundPieces.get(corner).get("top")[1] == False:
        if foundPieces.get(corner).get("left")[1] == False:
            topLeft = corner


#build the big grid
bigGrid = {}
startTileId = topLeft
nextTileId = startTileId
tileRow = 0
tileCol = 0

usedTileIds = []
while nextTileId != "":

    while nextTileId != "":
        usedTileIds.append(nextTileId)
        nextTileGrid = foundPieces.get(nextTileId).get("grid")
        print("  ")
        print("--------------------")
        print(nextTileId)
        for i in range(8):
            line = ""
            for ii in range(8):
                line = line + foundPieces.get(nextTileId).get("grid").get((ii, i))
            print(line)
        for key in nextTileGrid.keys():
            bigGridKey = (key[0] + tileCol, key[1] + tileRow)
            bigGrid[bigGridKey] = copy.deepcopy(nextTileGrid.get(key))

        lastTileId = nextTileId
        nextTileId = foundPieces.get(nextTileId).get("right")[2]
        tileCol = tileCol + 8

        if nextTileId == "" and tileCol < 96:
            print("Shit... again")
            bottom = foundPieces.get(lastTileId).get("bottom")[2]
            right = foundPieces.get(bottom).get("right")[2]
            top = foundPieces.get(right).get("top")[2]
            nextTileId = bottom




    tileCol = 0
    tileRow = tileRow + 8
    startTileId = foundPieces.get(startTileId).get("bottom")[2]
    if startTileId == "2557":
        print("shit")
    nextTileId = startTileId

initialCount = 0
for key in bigGrid.keys():
    if bigGrid.get(key) == '#':
        initialCount = initialCount + 1

# print("1951")
# for i in range(8):
#     line = ""
#     for ii in range(8):
#         line = line + foundPieces.get("1951").get("grid").get((ii,i))
#     print(line)


def printGrid():
    global bigGrid
    print("  ")
    print("  ")
    print("biggrid")
    for i in range(24):
        line = ""
        for ii in range(24):
            line = line + bigGrid.get((ii,i))
        print(line)
# for key in sorted(foundPieces.get("1951").get("grid").keys()):
#     print("KEY: {} VAL: {}".format(key,foundPieces.get("1951").get("grid").get(key)))

bigGridSize = sorted(bigGrid.keys(),reverse=True)[0][0] + 1
# bigGridSize = 24

monsterFound = False
# while monsterFound == False:
monstersFound = 0
for a in range(4):
    # printGrid()
    # if a == 2:
    #     printGrid()
    for i in range(bigGridSize):
        for ii in range(bigGridSize):
            monsterFound = True
            foundKeys = []
            for key in monster.keys():
                c1 = monster.get(key)
                if c1 == '#':
                    c2Key = (key[0] + ii, key[1] + i)
                    c2 = bigGrid.get(c2Key)
                    if c1 != c2:
                        monsterFound = False
                        # print("try next window")
                        break
                    else:
                        foundKeys.append(c2Key)
            if monsterFound == True:
                print("Monster Found")
                monstersFound = monsterFound + 1
                print("Starting Coord {}".format(foundKeys[0]))
                for key in foundKeys:
                    bigGrid[key] = 'O'
    if monsterFound:
        break
    else:
        bigGrid = copy.deepcopy(rotateGrid(bigGrid))

if monstersFound == 0:
    bigGrid = copy.deepcopy(flipGrid(bigGrid))

    for a in range(4):
        # printGrid()
        # if a == 2:
        #     printGrid()
        for i in range(bigGridSize):
            for ii in range(bigGridSize):
                monsterFound = True
                foundKeys = []
                for key in monster.keys():
                    c1 = monster.get(key)
                    if c1 == '#':
                        c2Key = (key[0] + ii, key[1] + i)
                        c2 = bigGrid.get(c2Key)
                        if c1 != c2:
                            monsterFound = False
                            # print("try next window")
                            break
                        else:
                            foundKeys.append(c2Key)
                if monsterFound == True:
                    print("Monster Found")
                    for key in foundKeys:
                        bigGrid[key] = 'O'
        if monsterFound:
            break
        else:
            bigGrid = copy.deepcopy(rotateGrid(bigGrid))

waterCnt = 0

for key in bigGrid.keys():
    if bigGrid.get(key) == '#':
        waterCnt = waterCnt + 1


print(corners)
print("Ans: {}".format(prod))
print("Water CNT: {}".format(waterCnt))
print("Initial Cnt: {}".format(initialCount))



# for i in range(bigGridSize):
#     for ii in range(bigGridSize):
#         testKey = (ii, i)
#         if testKey not in bigGrid.keys():
#             print(testKey)


missingKeys = set(foundPieces.keys()) - set(usedTileIds)

missingPieces = 0
for mkey in missingKeys:
    for gkey in foundPieces.get(mkey).get("grid"):
        if foundPieces.get(mkey).get("grid").get(gkey) == '#':
            missingPieces = missingPieces + 1

print("New Water CNT: {}".format(waterCnt + missingPieces))

print("--- %s seconds ---" % (time.time() - start_time))
