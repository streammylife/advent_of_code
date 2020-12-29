import time

start_time = time.time()
filepath = 'test'

imageTiles = {}
imageTile = {}
imageTile["grid"] = {}
imageTileKey = ()
y = 0

bufferingData = False

# def rotateTile(tile):
#     newTile = {}
#     for key in tile.keys():


with open(filepath) as fp:
    line = fp.readline()
    while line:

        if line.isspace():
            imageTiles[tileId] = imageTile.copy()
            imageTile = {}
            imageTile["grid"] = {}
            bufferingData = False
            y = 0
        else:
            line = line.split("\n")[0]
            if not bufferingData:
                tileId = line.split()[1].split(':')[0]
                bufferingData = True
            else:
                for x in range(len(line)):
                    imageTile.get("grid")[x, y] = line[x]
                y = y + 1

        line = fp.readline()

# ok... now I have all the tiles


for key in imageTiles.keys():
    grid = imageTiles.get(key).get("grid")

    left = map(lambda x: grid.get(x), filter(lambda x: x[0] == 0, sorted(grid.keys())))
    right = map(lambda x: grid.get(x), filter(lambda x: x[0] == 9, sorted(grid.keys())))
    top = map(lambda x: grid.get(x), filter(lambda x: x[1] == 0, sorted(grid.keys())))
    bottom = map(lambda x: grid.get(x), filter(lambda x: x[1] == 9, sorted(grid.keys())))

    edges = {"top": [top,False], "right": [right,False], "bottom": [bottom,False], "left": [left,False]}
    imageTiles.get(key)["edges"] = edges.copy()


# ok now I have all the edges

def getEdgesForCompare(tileDict, tileId):
    global imageTiles
    test = filter(lambda x: x[1] == False,tileDict.get(tileId).get("edges").values())
    edges = map(lambda x: tuple(x[0]), test)
    return edges


def compareEdges(dict1, id1, dict2, id2):
    edges1 = getEdgesForCompare(dict1, id1)
    edges2 = getEdgesForCompare(dict2, id2)
    matches = set(edges1) & set(edges2)
    return matches


#just grab an element
key = imageTiles.keys()[0]

#start with that and pop it from the list
matchTiles = {key: imageTiles.pop(key).copy()}

#now start iterating
newMatchTiles = {}
for key1 in matchTiles.keys():
    for key2 in imageTiles.keys():
        match = compareEdges(matchTiles, key1, imageTiles, key2)
        if len(match) == 1:
            print("Match Found {} and {}".format(key1, key2))
            newMatchTiles[key2] = imageTiles.get(key2).copy()

for key in newMatchTiles.keys():
    imageTiles.pop(key)

matchTiles.update(newMatchTiles)


match = sorted(match)

print("--- %s seconds ---" % (time.time() - start_time))
