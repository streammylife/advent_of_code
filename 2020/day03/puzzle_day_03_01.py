import re

filepath = 'input03'
lineIdxMax = 31
lines = 324
treeIdx = 0
lineIdx = 0
navRightMag = 3
navDownMag  = 1
treeSymb = '#'
treeCnt = 0


with open(filepath) as fp:
   line = fp.readline()
   treeIdx += 1
   while line:
#       print(treeIdx)
       lineIdx += navRightMag
       lineIdx = lineIdx % lineIdxMax
#       print("lineIdx: {}".format(lineIdx))
       line = fp.readline()
       treeIdx += 1
#       print("treeIdx: {}".format(treeIdx))
#       print(len(line))
       if(len(line) == lineIdxMax+1):
#           print(lineIdx)
#           print(line)
#           print(line[lineIdx-1])
           if(line[lineIdx] == '#'):
               treeCnt+=1

print(treeCnt)

#print(re.split('-| |: ', passwords[0]))

#for pw in passwords:
#    print(re.split('- | |: ', pw))
