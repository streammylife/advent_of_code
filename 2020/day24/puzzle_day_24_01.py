import time

start_time = time.time()
filepath = 'input'

def createNewTile(key,color):
    tile = {}
    east = key[0]
    north = key[1]
    tile["color"] = color
    tile["adj"] = []
    tile["adj"].append((east + 1, north))
    tile["adj"].append((east - 1, north))
    tile["adj"].append((east + .5, north + 1))
    tile["adj"].append((east + .5, north - 1))
    tile["adj"].append((east - .5, north + 1))
    tile["adj"].append((east - .5, north - 1))
    return tile

with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    tiles = {}
    while line:
        east = 0.0
        north = 0.0
        dir = ""
        tmpKey = {}
        # print("New Line")
        # print(line)
        for c in line:
            dir = dir + c

            if dir in ["ne", "nw", "se", "sw", "w", "e"]:

                if 'n' in dir:
                    north = north + 1.0
                elif 's' in dir:
                    north = north - 1.0

                if 'e' in dir:
                    east = east + (1.0 / len(dir))
                elif 'w' in dir:
                    east = east - (1.0 / len(dir))

                dir = ""

            elif dir == '\n':

                # tileKey = "{},{}".format(east,north)
                tileKey = (east,north)
                 # print(tileKey)
                east = 0
                north = 0

                tile = {}

                # for key in sorted(tmpKey.keys()):
                #     tileKey = tileKey + "{} ".format(tmpKey.get(key))
                tile = tiles.get(tileKey)

                if tile != None:
                    if tile.get("color") == "black":
                        tile["color"] = "white"
                    else:
                        tile["color"] = "black"
                else:
                    tile = createNewTile(tileKey, "black").copy()

                tiles[tileKey] = tile

        line = fp.readline()

blackCnt = 0
for key in tiles.keys():
    if tiles.get(key).get("color") == "black":
        blackCnt = blackCnt + 1

def createNewAdjTiles(tileDict):
    #create new adj tiles
    newTiles = {}
    for key1 in tileDict.keys():
        for key2 in tileDict.get(key1)["adj"]:
            if(tileDict.get(key2) == None):
                newTiles[key2] = createNewTile(key2, "white").copy()
    return newTiles.copy()

tiles.update(createNewAdjTiles(tiles))



for i in range(100):
    print(i)
    newTiles = {}
    blackTileCnt = 0
    for key1 in tiles.keys():
        tile = tiles.get(key1)
        color = tile.get("color")
        blackCnt = 0
        newTiles[key1] = tile.copy()
        for key2 in tile.get("adj"):
            tile2 = tiles.get(key2)
            if tile2 != None:
                if tile2.get("color") == "black":
                    blackCnt = blackCnt + 1

        if color == "black":
            if blackCnt == 0 or blackCnt > 2:
                newTiles[key1]["color"] = "white"
            else:
                blackTileCnt = blackTileCnt + 1
        else:
            if blackCnt == 2:
                newTiles[key1]["color"] = "black"
                blackTileCnt = blackTileCnt + 1
    tiles = newTiles.copy()

    tiles.update(createNewAdjTiles(tiles))






print(blackTileCnt)
print("--- %s seconds ---" % (time.time() - start_time))
