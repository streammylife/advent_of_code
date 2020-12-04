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
treeCntProd = 1

navRightMagSlopes = [1,3,5,7,1]
navDownMags = [1,1,1,1,2]

for x in range(0,5):
    navRightMag = navRightMagSlopes[x]
    navDownMag = navDownMags[x]
    print("navRightMag: {}".format(navRightMag))
    print("navDownMag: {}".format(navDownMag))
    print("---")


    with open(filepath) as fp:
       line = fp.readline()
       treeIdx += 1
       while line:
    #       print(treeIdx)
           lineIdx += navRightMag
           lineIdx = lineIdx % lineIdxMax
    #       print("lineIdx: {}".format(lineIdx))
           line = fp.readline()
           if(navDownMag == 2):
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
    treeCntProd *= treeCnt
    treeCnt = 0
    lineIdx = 0

print(treeCntProd)

#print(re.split('-| |: ', passwords[0]))

#for pw in passwords:
#    print(re.split('- | |: ', pw))
