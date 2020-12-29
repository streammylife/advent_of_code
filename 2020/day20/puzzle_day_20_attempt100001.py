import time
import copy

start_time = time.time()
filepath = 'test'

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



def reorientGrid(tmpTileId, tmpTiles, searchRnd):
    """

    :type tmpTiles: object
    """
    tmpTileGrid = tmpTiles.get(tmpTileId).get("grid")
    newTileGrid = copy.deepcopy(tmpTileGrid)

    if searchRnd > 2:
        #gotta flip it
        for key in tmpTileGrid.keys():
            newKey = ((key[0] - 7) % 8,key[1])
            newTileGrid[newKey] = copy.deepcopy(tmpTileGrid[key])
        rotations = searchRnd - 3
    else:
        rotations = searchRnd

    for i in range(rotations):
        for key in tmpTileGrid.keys():
            newKey = ((key[1] - 7) % 8,key[0])
            newTileGrid[newKey] = copy.deepcopy(tmpTileGrid[key])

    tmpTiles.get(tmpTileId)["grid"] = copy.deepcopy(newTileGrid)

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
                rotateTile(key1, tiles)
                if searchRound == 3 or searchRound == 7:
                    flipTileX(key1,tiles)
                searchRound = searchRound + 1
            else:
                reorientGrid(key1, tiles, searchRound)

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
startTileId = corner
nextTileId = startTileId
tileRow = 0
tileCol = 0
while nextTileId != "":
    print(nextTileId)

    nextTileGrid = foundPieces.get(nextTileId).get("grid")
    while nextTileId != "":
        for key in nextTileGrid.keys():
            bigGrid[key[0] + tileCol, key[1] + tileRow] = copy.deepcopy(nextTileGrid.get(key))
        nextTileId = foundPieces.get(nextTileId).get("right")[2]
        tileCol = tileCol + 1

    tileCol = 0
    tileRow = tileRow + 1
    startTileId = foundPieces.get(startTileId).get("bottom")[2]
    nextTileId = startTileId





print(corners)
print("Ans: {}".format(prod))







print("--- %s seconds ---" % (time.time() - start_time))
