filepath = 'input'
data = []

memory = {}
mask = ""
maskOffset = 7


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if(line.find("mask = ") > -1):
           mask = line[maskOffset:]
           print(mask)
       else:
           memIdxStart = line.find('[') + 1
           memIdxEnd = line.find(']')
           memIdx = int(line[memIdxStart:memIdxEnd])

           memValOffset = line.find('=') + 2
           memVal = int(line[memValOffset:])
           
           memValBin = "{0:b}".format(memVal)
           memValBin = memValBin.zfill(36)
           print(memVal)
           print(memIdx)
           print(memValBin)
           valToWrite = ""
           for i in range(len(memValBin)):
               if(mask[i] == 'X'):
                   tmpVal = memValBin[i]
               else:
                   tmpVal = mask[i]
               valToWrite = valToWrite + tmpVal
           print(valToWrite)
           tmpVal = int(valToWrite,2)
           print(tmpVal)
           memory[memIdx] = tmpVal

       print("  ")

       line = fp.readline()

memTotal = 0
for key in memory:
    memTotal = memTotal + memory[key]

print(memTotal)
