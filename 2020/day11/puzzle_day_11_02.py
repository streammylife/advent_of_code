filepath = 'input'
adapters = []
marginHigh = 3

# windowLen = 25
# invalidNum = 57195069
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       number = int(line)
       adapters.append(number)
       line = fp.readline()

adapters.sort(reverse=True)
#print(adapters[0] + marginHigh)
#print(adapters)

oneJGaps = 0
threeJGaps = 0
startJ = 0

lastVal = startJ

paths = []
cnt = 0

# print(adapters)
# print("------")

for i in range(len(adapters)):
    numbers = []
    for ii in range(1,4):
        searchVal = adapters[i] - ii
        if searchVal in adapters:
            numbers.append(searchVal)
    #print(numbers)
    paths.append(numbers)

print(paths)
#
# print(paths)

uniquePaths = 0
localCnts = []


paths.sort()


localCnts.append(1)
i = 0

adapters.sort()
# print(adapters)
# print(paths)
# print("------")
paths[0].append(1)
for path in paths:
    if(i == 0):
        localCnt = 1
    else:
        localCnt = 0
        for subPath in path:
            localCnt = localCnt + localCnts[adapters.index(subPath) + 1]
            # print("Subpath - {}, idx ={} localCnt - {}".format(subPath,adapters.index(subPath), localCnts[adapters.index(subPath)]))
            #print(localCnts[adapters.index(subPath)])
    # print("Val {}: Path:{} localCnt - {}".format(adapters[i], path, localCnt))
    # print(localCnt)
    # print("------------")
    localCnts.append(localCnt)
    i = i + 1

print(adapters)
print(localCnts)
