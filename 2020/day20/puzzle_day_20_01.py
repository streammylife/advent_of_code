import time

start_time = time.time()


filepath = 'test'
numbers = []

grids = {}

def rotateGrid(grid):
    tmp = grid.get(3)
    for key in reversed(range(1,4)):
        grid[key] = grid.get(key - 1)
    grid[0] = tmp

def flipGridY(grid):
    tmpGrid = grid.get(2)
    grid[2] = grid.get(0)
    grid[0] = tmpGrid
    grid[1] = grid.get(1)[::-1]
    grid[3] = grid.get(3)[::-1]

def flipGridX(grid):
    tmpGrid = grid.get(3)
    grid[3] = grid.get(1)
    grid[1] = tmpGrid
    grid[0] = grid.get(0)[::-1]
    grid[2] = grid.get(2)[::-1]

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
                   grids[key] = grid.copy()
                   for key in grid.keys():
                       grid[key]["match"] = False

               y = y + 1

       line = fp.readline()


# print("Grids: {}")
# for key in grids.keys():
#     print(key)
#     print(grids.get(key))

#Find edge matches for the first grid
key = grids.keys()[0]
grid = grids.get(key)

#start with one piece
puzzle = {}
puzzle[key] = grid.copy()
grids.pop(key)

print(key)

# testRotate(grid)


matchKeys = []

complete = False
while complete == False:
    complete = True
    matchKey = []
    for puzzleKey in puzzle.keys():
        puzzlePiece = puzzle.get(key)
        for edgeKey in puzzlePiece.keys():
            edge = puzzlePiece.get(edgeKey)
            #first check if edge has match
            if edge.get("match") == False:
                for loosePuzzleKey in grids.keys():
                    loosePuzzlePiece = grids.get(loosePuzzleKey)
                    for looseEdgeKey in loosePuzzlePiece.keys():
                        looseEdge = loosePuzzlePiece.get(looseEdgeKey)
                        if looseEdge.get("edge") == edge.get("edge"):
                            looseEdge["match"] = True
                            edge["match"] = True
                            matchKeys.append(loosePuzzleKey)
                            complete = False

    matchKeys = list(dict.fromkeys(matchKeys))
    for matchKey in matchKeys:
        puzzle[matchKey] = grids.get(matchKey)
        grids.pop(matchKey)


# print("flipping x")
#
# for puzzleKey in puzzle.keys():
#     puzzlePiece = puzzle.get(key)
#     for edgeKey in puzzlePiece.keys():
#         edge = puzzlePiece.get(edgeKey)
#         #first check if edge has match
#         if edge.get("match") == False:
#             for loosePuzzleKey in grids.keys():
#                 loosePuzzlePiece = grids.get(loosePuzzleKey)
#                 flipGridX((loosePuzzlePiece))
#                 for looseEdgeKey in loosePuzzlePiece.keys():
#                     looseEdge = loosePuzzlePiece.get(looseEdgeKey)
#                     if looseEdge.get("edge") == edge.get("edge"):
#                         looseEdge["match"] = True
#                         edge["match"] = True
#                         matchKeys.append(loosePuzzleKey)
#
# matchKeys = list(dict.fromkeys(matchKeys))
# for matchKey in matchKeys:
#     puzzle[matchKey] = grids.get(matchKey)
#     grids.pop(matchKey)


#
# for rowKey in sorted(grid.keys()):
#     edge1 = grid.get(rowKey)
#     print(" ")
#     print("------------")
#     print("Edge: {}".format(rowKey))
#     print("Edge to search: {}".format(edge1))
#     print(" ")
#     for gridKey in grids.keys()[1:]:
#         tmpGrid = grids.get(gridKey)
#         for rowKey2 in tmpGrid.keys():
#             edge2 = tmpGrid.get(rowKey2)
#             if edge1 == edge2:
#                 print("Grid: {} Edge: {}".format(gridKey, rowKey2))
#                 print("Edge: {}".format(edge2))
#                 print("Match Found")

# print("flip x")
# flipGridX(grid)
#
# for rowKey in grid.keys():
#     edge1 = grid.get(rowKey)
#     print(" ")
#     print("------------")
#     print("Edge to search: {}".format(edge1))
#     print(" ")
#     for gridKey in grids.keys()[1:]:
#         tmpGrid = grids.get(gridKey)
#         for rowKey2 in tmpGrid.keys():
#             edge2 = tmpGrid.get(rowKey2)
#             if edge1 == edge2:
#                 print("Grid: {} Edge: {}".format(gridKey, rowKey2))
#                 print("Edge: {}".format(edge2))
#                 print("Match Found")
#
# print("flip y")
# flipGridY(grid)
#
# for rowKey in grid.keys():
#     edge1 = grid.get(rowKey)
#     print(" ")
#     print("------------")
#     print("Edge to search: {}".format(edge1))
#     print(" ")
#     for gridKey in grids.keys()[1:]:
#         tmpGrid = grids.get(gridKey)
#         for rowKey2 in tmpGrid.keys():
#             edge2 = tmpGrid.get(rowKey2)
#             if edge1 == edge2:
#                 print("Grid: {} Edge: {}".format(gridKey, rowKey2))
#                 print("Edge: {}".format(edge2))
#                 print("Match Found")


print("--- %s seconds ---" % (time.time() - start_time))