import time

start_time = time.time()
filepath = 'test2'

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

    edges = {"top": top, "right": right, "bottom": bottom, "left": left}
    imageTiles.get(key)["edges"] = edges.copy()


# ok now I have all the edges

def getEdgesForCompare(tileId):
    global imageTiles
    edges = map(lambda x: tuple(x), imageTiles.get(tileId).get("edges").values())
    return edges


def compareEdges(id1, id2):
    edges1 = getEdgesForCompare(id1)
    edges2 = getEdgesForCompare(id2)
    matches = set(edges1) & set(edges2)
    return matches


# edges1 = getEdgesForCompare("2473")
# edges2 = map(lambda x: tuple(x), imageTiles.get("1171").get("edges").values())

match = compareEdges("2473", "1171")

match = sorted(match)

print("--- %s seconds ---" % (time.time() - start_time))
