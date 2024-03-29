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



with open(filepath) as fp:
    line = fp.readline()
    tile = {}
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

            tiles[tileId] = tile.copy()
            tile = {}
            tileId = ""
            top = ""
            right = ""
            bottom = ""
            left = ""
            tileLine = 0

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
for corner in corners:
    prod = prod * int(corner)


print(corners)
print("Ans: {}".format(prod))


print("--- %s seconds ---" % (time.time() - start_time))
