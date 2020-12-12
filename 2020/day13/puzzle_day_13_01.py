import time

filepath = 'input'

curDir = 'E'
dirs = []

eastSum = 0
northSum = 0

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       tmpDir = []
       tmpDir.append(line[0])
       tmpDir.append(int(line[1:]))
       dirs.append(tmpDir)
       line = fp.readline()

dirArray = ['N', 'E', 'S', 'W']

waypoint = [10,1]

for dir in dirs:
    tmpDir = dir[0]
    tmpVal = dir[1]
    mag = 0

    if tmpDir == 'F':
        mag = tmpVal
        tmpDir = curDir
    elif tmpDir == 'L' or tmpDir == 'R':
        dirChange = tmpVal / 90
        curDirArrayPos = dirArray.index(curDir)
        if tmpDir == 'L':
            curDir = dirArray[(curDirArrayPos - dirChange) % 4]
        if tmpDir == 'R':
            curDir = dirArray[(curDirArrayPos + dirChange) % 4]
    # elif tmpDir == 'E' or tmpDir == 'W':
    #     curDir = tmpDir
    #     mag = tmpVal
    else:
        mag = tmpVal

    if mag > 0:
        if tmpDir == 'N':
            northSum = northSum + mag
        elif tmpDir == 'S':
            northSum = northSum - mag
        elif tmpDir == 'E':
            eastSum = eastSum + mag
        elif tmpDir == 'W':
            eastSum = eastSum - mag


    print("facing: {}".format(curDir))
    print("moved: {}".format(tmpDir))
    print("mag: {}".format(mag))
    print("eastSum: {}".format(eastSum))
    print("northSum: {}".format(northSum))
    print("    ")

print(abs(northSum) + abs(eastSum))
