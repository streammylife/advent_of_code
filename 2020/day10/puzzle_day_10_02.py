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
paths = []
cnt = 0
for i in range(len(adapters)):
    numbers = []
    for ii in range(1,4):
        searchVal = adapters[i] - ii
        if searchVal in adapters:
            numbers.append(searchVal)
    paths.append(numbers)

print(paths)

localCnts = []


paths.sort()


localCnts.append(1)
i = 0

adapters.sort()
paths[0].append(1)
for path in paths:
    if(i == 0):
        localCnt = 1
    else:
        localCnt = 0
        for subPath in path:
            localCnt = localCnt + localCnts[adapters.index(subPath) + 1]
    localCnts.append(localCnt)
    i = i + 1

print(adapters)
print(localCnts)
