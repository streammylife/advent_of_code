import time

start_time = time.time()
filepath = 'input'

gamma = 0
eps = 0

oneCnt = [0] * 12
zeroCnt = [0] * 12

oxy = []
co2 = []

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       num = int(line, 2)
       oxy.append(num)
       co2.append(num)
       line = fp.readline()

oxy.sort()
co2.sort()

filter = 0
for i in range(12):
    oxyCnt = 0

    nextVal = (1 << (11 - i))
    filter = filter + nextVal

    for num in oxy:


        if num < filter:
            oxyCnt = oxyCnt + 1
        else:
            break
    if oxyCnt > (len(oxy) / 2):
        oxy = oxy[:oxyCnt]
        filter = filter - nextVal
    else:
        oxy = oxy[oxyCnt:]

    if len(oxy) == 1:
        break;

filter = 0
for i in range(12):
    co2Cnt = 0

    nextVal = (1 << (11 - i))
    filter = filter + nextVal

    for num in co2:
        if num < filter:
            co2Cnt = co2Cnt + 1
        else:
            break

    if co2Cnt <= (len(co2) / 2):
        co2 = co2[:co2Cnt]
        filter = filter - nextVal
    else:
        co2 = co2[co2Cnt:]

    if len(co2) == 1:
        break;

lsr = co2[0] * oxy[0]

#1748394 is too low
#1800151 is correct

print("--- %s seconds ---" % (time.time() - start_time))