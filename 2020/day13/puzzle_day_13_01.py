filepath = 'input'
data = []
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       data.append(line)
       line = fp.readline()

timeStamp = int(data[0])
buses = data[1].split("\n")[0].split(',')
print(timeStamp)
print(buses)

closestBus = [0,100000000]
for bus in buses:
    if bus != 'x':
        busNum = int(bus)
        diff = busNum - (timeStamp % busNum)
        print(diff)
        if diff < closestBus[1]:
            closestBus[0] = busNum
            closestBus[1] = diff

print closestBus[0] * closestBus[1]
