filepath = 'test2'
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

forkCnt = 0

print(adapters)
for a in adapters:
    print("----")
    print(a)
    localForkCnt = 0
    if(a - 3) in adapters:
        localForkCnt = localForkCnt + 1
    if(a - 2) in adapters:
        localForkCnt = localForkCnt + 1
    if(a - 1) in adapters:
        localForkCnt = localForkCnt + 1
    if localForkCnt > 1:
        print(localForkCnt)
        forkCnt = forkCnt + localForkCnt

print(forkCnt + 1)
