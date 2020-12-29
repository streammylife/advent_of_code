import time

start_time = time.time()
filepath = 'test'

tiles = {}

edgeMatches = {"top": "bottom", "right": "left", "bottom": "top", "left": "right"}

def rotateTile(tmpTileId, tmpTiles):
    tmpTile = tmpTiles.get(tmpTileId)
    edgeList = ["top", "right", "bottom", "left"]

    for edge in edgeList:
        tmpEdge = tmpTile.get(edge)
        tmpEdge[0] = tmpEdge[0] + 1 % 4

def flipTileX(tmpTileId, tmpTiles):
    tmpTile = tmpTiles.get(tmpTileId)
    tmpEdge = tmpTile.get("left")



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

print("--- %s seconds ---" % (time.time() - start_time))
