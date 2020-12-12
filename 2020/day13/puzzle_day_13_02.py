import time

filepath = 'input'

curDir = 'E'
instructions = []

eastSum = 0
northSum = 0

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       tmpDir = []
       tmpDir.append(line[0])
       tmpDir.append(int(line[1:]))
       instructions.append(tmpDir)
       line = fp.readline()

dirArray = ['N', 'E', 'S', 'W']


waypointDirs = [0,2]
waypoint = ['E',10,'N',1]

for instruction in instructions:
    print(instruction)

    tmpInstrCmd = instruction[0]
    tmpInstrVal = instruction[1]
    if tmpInstrCmd == 'F':
        for i in range(tmpInstrVal):
            if waypoint[0] == 'E':
                eastSum = eastSum + waypoint[1]
            elif waypoint[0] == 'W':
                eastSum = eastSum - waypoint[1]
            elif waypoint[0] == 'N':
                northSum = northSum + waypoint[1]
            elif waypoint[0] == 'S':
                northSum = northSum - waypoint[1]

            if waypoint[2] == 'E':
                eastSum = eastSum + waypoint[3]
            elif waypoint[2] == 'W':
                eastSum = eastSum - waypoint[3]
            elif waypoint[2] == 'N':
                northSum = northSum + waypoint[3]
            elif waypoint[2] == 'S':
                northSum = northSum - waypoint[3]

    elif tmpInstrCmd == 'L' or tmpInstrCmd == 'R':
        dirChange = tmpInstrVal / 90
        curDirArrayPos = dirArray.index(waypoint[0])
        if tmpInstrCmd == 'L':
            waypoint[0] = dirArray[(curDirArrayPos - dirChange) % 4]
        if tmpInstrCmd == 'R':
            waypoint[0] = dirArray[(curDirArrayPos + dirChange) % 4]

        curDirArrayPos = dirArray.index(waypoint[2])
        if tmpInstrCmd == 'L':
            waypoint[2] = dirArray[(curDirArrayPos - dirChange) % 4]
        if tmpInstrCmd == 'R':
            waypoint[2] = dirArray[(curDirArrayPos + dirChange) % 4]

    elif tmpInstrCmd == 'E':
        for waypointDir in waypointDirs:
            if waypoint[waypointDir] == 'E':
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] + tmpInstrVal
            if waypoint[waypointDir] == 'W':
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] - tmpInstrVal
                if waypoint[waypointDir + 1] < 0:
                    waypoint[waypointDir] = 'E'
                    waypoint[waypointDir + 1] = abs(waypoint[waypointDir + 1])
    elif tmpInstrCmd == 'W':
        for waypointDir in waypointDirs:
            if waypoint[waypointDir] == 'W':
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] + tmpInstrVal
            if waypoint[waypointDir] == 'E':
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] - tmpInstrVal
                if waypoint[waypointDir + 1] < 0:
                    waypoint[waypointDir] = 'W'
                    waypoint[waypointDir + 1] = abs(waypoint[waypointDir + 1])
    elif tmpInstrCmd == 'N':
        for waypointDir in waypointDirs:
            if waypoint[waypointDir] == 'N':
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] + tmpInstrVal
            if waypoint[waypointDir] == 'S':
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] - tmpInstrVal
                if waypoint[waypointDir + 1] < 0:
                    waypoint[waypointDir] = 'N'
                    waypoint[waypointDir + 1] = abs(waypoint[waypointDir + 1])
    elif tmpInstrCmd == 'S':
        for waypointDir in waypointDirs:
            if waypoint[waypointDir] == 'S':
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] + tmpInstrVal
            if waypoint[waypointDir] == 'N':
                # print("here")
                waypoint[waypointDir + 1] = waypoint[waypointDir + 1] - tmpInstrVal
                # print(waypoint[waypointDir + 1])
                if waypoint[waypointDir + 1] < 0:
                    waypoint[waypointDir] = 'S'
                    waypoint[waypointDir + 1] = abs(waypoint[waypointDir + 1])
    print(waypoint)
    print("eastSum: {}".format(eastSum))
    print("northSum: {}".format(northSum))
    print("    ")


print(abs(northSum) + abs(eastSum))
