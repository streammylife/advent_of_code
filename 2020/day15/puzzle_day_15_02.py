import time
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
           startMask = line[maskOffset:len(line)-1]
           print("Mask: {}".format(mask))
       else:
           print("--------")
           print(" ")
           memIdxStart = line.find('[') + 1
           memIdxEnd = line.find(']')
           memIdx = int(line[memIdxStart:memIdxEnd])
           memIdxBin = "{0:b}".format(memIdx)
           memIdxBin = memIdxBin.zfill(36)


           memValOffset = line.find('=') + 2
           memVal = int(line[memValOffset:])

           newMask = ""
           for i in range(len(memIdxBin)):
               if(startMask[i] == '0'):
                   tmpVal = memIdxBin[i]
               else:
                   tmpVal = startMask[i]
               newMask = newMask + tmpVal

           # print("NewMask: {}".format(newMask))

           complete = False
           searchStart = 0
           newMasks = []
           newMasks.append(newMask)
           while(complete == False):
               complete = True
               tmpMasks = []
               #print("New Masks: {}".format(newMasks))
               for mask in newMasks:
                   for i in range(searchStart,len(mask)):
                       if(mask[i]) == 'X':
                           # s = s[:index] + newstring + s[index + 1:]
                           tmpMask = mask[:i] + '0' + mask[i+1:];
                           tmpMasks.append(tmpMask)
                           tmpMask = mask[:i] + '1' + mask[i+1:];
                           tmpMasks.append(tmpMask)
                           complete = False
                           break
               if(complete == False):
                   newMasks = tmpMasks


           print("MemVal: {}".format(memVal))
           for mask in newMasks:
               memAddr = int(mask,2)
               print("MemAddr: {}".format(memAddr))
               memory[memAddr] = memVal

           # print(newMasks)


       # valToWrite = valToWrite + tmpVal
       #
       #
       #     memValBin = "{0:b}".format(memVal)
       #     memValBin = memValBin.zfill(36)
       #     print(memVal)
       #     print(memIdx)
       #     print(memValBin)
       #     valToWrite = ""
       #     for i in range(len(memValBin)):
       #         if(mask[i] == 'X'):
       #             tmpVal = memValBin[i]
       #         else:
       #             tmpVal = mask[i]
       #         valToWrite = valToWrite + tmpVal
       #     print(valToWrite)
       #     tmpVal = int(valToWrite,2)
       #     print(tmpVal)
       #     memory[memIdx] = tmpVal
       #
       # print("  ")

       line = fp.readline()

memTotal = 0
for key in memory:
    memTotal = memTotal + memory[key]

print("--------")
print(" ")
print("Sum: {}".format(memTotal))
