import time

start_time = time.time()
filepath = 'test'

loosePieces = {}

def rotateGrid(grid):
    tmp = grid.get("west")
    for key in reversed(range(1,4)):
        grid[key] = grid.get(key - 1)
    grid[0] = tmp


#get all the pieces
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
               grid["north"] = {}
               grid["east"] = {}
               grid["south"] = {}
               grid["west"] = {}
           else:
               line = line.split("\n")[0]
               if y == 0:
                   grid["north"]["edge"] = line
                   grid["east"]["edge"] = ""
                   grid["west"]["edge"] = ""

               grid["east"]["edge"] = grid["east"].get("edge") + line[9]
               grid["west"]["edge"] = grid["west"].get("edge") + line[0]

               if y == 9:
                   grid["south"]["edge"] = line
                   loosePieces[key] = grid.copy()
                   for key in grid.keys():
                       grid[key]["match"] = None
                       if key == "east":
                           grid[key]["matchKey"] = "west"
                       elif key == "west":
                           grid[key]["matchKey"] = "east"
                       elif key == "north":
                           grid[key]["matchKey"] = "south"
                       else:
                           grid[key]["matchKey"] = "north"

               y = y + 1

       line = fp.readline()

foundPieces = {}
key = loosePieces.keys()[0]

#pick a piece to start with
foundPieces[key] = loosePieces.pop(key)

for key1 in foundPieces.keys():
    p1 = foundPieces.get(key1)
    for key2 in p1.keys():
        edge = p1.get(key2)
        if edge.get("match") == None:
            for key3 in loosePieces.keys():
                lp = loosePieces.get(key3)
                for i in range(4):
                    checkEdge = edge.get("matchKey")
                    edge2 = lp.get(checkEdge)
                    if edge.get("edge") == edge2.get("edge"):
                        print(checkEdge)


print("--- %s seconds ---" % (time.time() - start_time))
