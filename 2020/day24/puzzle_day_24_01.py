import time

start_time = time.time()
filepath = 'test'


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   tiles = {}
   while line:
       east = 0
       north = 0
       dir = ""
       tmpKey = {}
       for c in line:
           dir = dir + c
           if dir in ["ne", "nw", "se", "sw", "w", "e"]:
               if tmpKey.get(dir) == None:
                   tmpKey[dir] = 1
               else:
                   tmpKey[dir] = tmpKey[dir] + 1
               dir = ""
           elif dir == '\n':

               tileKey = ""
               for key in sorted(tmpKey.keys()):
                   tileKey = tileKey + "{} ".format(tmpKey.get(key))
               tile = tiles.get(tileKey)

               if tile != None:
                   if tile == "black":
                       tiles[tileKey] = "white"
                   else:
                       tiles[tileKey] = "black"
               else:
                   tiles[tileKey] = "black"
       line = fp.readline()



print("--- %s seconds ---" % (time.time() - start_time))