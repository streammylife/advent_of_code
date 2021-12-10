import time

start_time = time.time()
filepath = 'input_ex'

segments = []


def line_intersection(line1, line2):
    res = False
    resPoint = (0, 0)
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False, (0, 0)

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return True, (x, y)


with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        line = line.strip('\n')
        line = line.split(' -> ')

        p1 = map(int, line[0].split(','))
        p2 = map(int, line[1].split(','))

        #m = (p2[1] - p1[1]) / p

        if p1[0] == p2[0]:
            segments.append(((p1, p2), None))
        elif p1[1] == p2[1]:
            segments.append(((p1, p2), 0))

        line = fp.readline()

# Old Solution
# grid = {}
# lineCnt = 0
# with open(filepath) as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        line = line.strip('\n')
#        line = line.split(' -> ')
#
#        p1 = map(int, line[0].split(','))
#        p2 = map(int, line[1].split(','))
#
#        # x1 = 0
#        # y1 = 0
#        # x2 = 0
#        # y2 = 0
#
#        if(p1[0] == p2[0]):
#            y1 = p1[1]
#            y2 = p2[1]
#            if p2[1] < p1[1]:
#                y1 = p2[1]
#                y2 = p1[1]
#            for yOff in range(y2 - y1 + 1):
#                key = (p1[0], y1+yOff)
#                if key in grid.keys():
#                    grid[key] = grid[key] + 1
#                else:
#                    grid[key] = 1
#        elif (p1[1] == p2[1]):
#            x1 = p1[0]
#            x2 = p2[0]
#            if p2[0] < p1[0]:
#                x1 = p2[0]
#                x2 = p1[0]
#            for xOff in range(x2 - x1 + 1):
#                key = (x1 + xOff, p1[1])
#                if key in grid.keys():
#                    grid[key] = grid[key] + 1
#                else:
#                    grid[key] = 1
#
#        lineCnt = lineCnt + 1
#        if(lineCnt % 50 == 0):
#            print("LineCnt: {0}", lineCnt)
#            print("--- %s seconds ---" % (time.time() - start_time))
#        line = fp.readline()
#
# overlap = 0
#
# for key in grid.keys():
#     if grid[key] >= 2:
#         overlap = overlap + 1

intersections = []

for i in range(len(segments)):
    for ii in range(i + 1, len(segments), 1):
       if segments[i][1] == segments[ii][i]:
           print("Slopes are the same")



print("--- %s seconds ---" % (time.time() - start_time))
