import time

start_time = time.time()


filepath = 'test'
numbers = []

loosePieces = {}

def rotateGrid(grid):
    tmp = grid.get(3)
    for key in reversed(range(1,4)):
        grid[key] = grid.get(key - 1)
    grid[0] = tmp

def flipGridY(grid):
    tmpGrid = grid.get(2)
    grid[2] = grid.get(0)
    grid[0] = tmpGrid
    grid[1]["edge"] = grid.get(1).get("edge")[::-1]
    grid[3]["edge"] = grid.get(3).get("edge")[::-1]

def flipGridX(grid):
    tmpGrid = grid.get(3)
    grid[3] = grid.get(1)
    grid[1] = tmpGrid
    grid[0]["edge"] = grid.get(0).get("edge")[::-1]
    grid[2]["edge"] = grid.get(2).get("edge")[::-1]

def printGrid(grid):
    for key in sorted(grid.keys()):
        print(grid.get(key))

def testRotate(grid):
    print("test rotate")
    print("starting grid:")
    printGrid(grid)

    rotateGrid(grid)

    print("After 1 rotation")
    printGrid(grid)
    rotateGrid(grid)
    rotateGrid(grid)
    rotateGrid(grid)
    print("After 4 rotations")
    printGrid(grid)




with open(filepath) as fp:
   line = fp.readline()
   foundKey = False
   cnt = 1
   x=0
   y=0
   grid = {}
   while line:
       #Build the grid edges bc that's all I care about right now
       if line.isspace():
           foundKey = False
       else:
           if foundKey == False:
               key = line.split()[1].split(':')[0]
               foundKey = True
               y = 0
               grid[0] = {}
               grid[1] = {}
               grid[2] = {}
               grid[3] = {}
           else:
               line = line.split("\n")[0]
               if y == 0:
                   grid[0]["edge"] = line
                   grid[1]["edge"] = ""
                   grid[3]["edge"] = ""

               grid[1]["edge"] = grid[1].get("edge") + line[9]
               grid[3]["edge"] = grid[3].get("edge") + line[0]

               if y == 9:
                   grid[2]["edge"] = line
                   loosePieces[key] = grid.copy()
                   for key in grid.keys():
                       grid[key]["match"] = False

               y = y + 1

       line = fp.readline()

print(loosePieces)

allPieces = loosePieces.copy()


def findMatches(key1):
    matchFound = False
    for key2 in loosePieces.keys():
        if key1 != key2:
            for edge1 in loosePieces.get(key1).keys():
                edge1 = loosePieces.get(key1).get(edge1)
                if edge1.get("match") == False:
                    for edge2 in loosePieces.get(key2).keys():
                        edge2 = loosePieces.get(key2).get(edge2)
                        if edge2.get("match") == False:
                            if edge1.get("edge") == edge2.get("edge"):
                                matchFound = True
                                edge1["match"] = True
                                edge2["match"] = True
                                foundPieces

    return matchFound

for key1 in loosePieces.keys():
    matchFound = findMatches(key1)

    #no match so flip it
    if matchFound == False:
        flipGridY(loosePieces.get(key1))
        matchFound = findMatches(key1)

    #no match so flip it
    if matchFound == False:
        flipGridX(loosePieces.get(key1))
        matchFound = findMatches(key1)



print("--- %s seconds ---" % (time.time() - start_time))