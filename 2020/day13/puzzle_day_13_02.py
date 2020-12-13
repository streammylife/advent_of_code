import time

filepath = 'test'
data = []
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       data.append(line)
       line = fp.readline()

timeStamp = int(data[0])
buses = data[1].split("\n")[0].split(',')
# print(timeStamp)
# print(buses)

complete = False

i = 1

testVal = 1
# for i in range(0,len(buses)):
    # testVal = testVal + i
    # #print(testVal)
    # if buses[i] != 'x':
    #     busNum = int(buses[i])
    #     if (testVal % busNum) != 0:
    #         testVal = testVal * busNum
    #
    # print(testVal)


busVals = []
for i in range(len(buses)):
    busVal = []
    if buses[i] != 'x':
        busVal.append(i)
        busVal.append(int(buses[i]))
        busVals.append(busVal)
print(busVals)

busMults = []
for busVal in busVals:
    idxMatch = busVal[0] + busVal[1]
    mult = 1
    for busVal2 in busVals:
        if busVal2[0] == idxMatch:
            mult = busVal2[1]
            break
    busMults.append(mult)

print(busMults)



complete = False
multFact = 1

# while complete == False:
#     complete = True
#     startVal = (busVals[0][1] * busMults[0]) + (busVals[0][1] * multFact - 1)
#     for i in range(1,len(busVals)):
#
#     multFact = multFact + 1
#
# print(startVal)

complete = False
while complete != True:
    # print("---------")
    complete = True
    startTestVal = int(buses[0]) * i
    for ii in range(1,len(buses)):
        testVal = startTestVal + ii
        if(buses[ii] != 'x'):
            if testVal >= int(buses[ii]):
                if (testVal % int(buses[ii])) != 0:
                    complete = False
                    break
                # else:
                #     print("testVal {}".format(testVal))
                #     print("number check {}".format(int(buses[ii])))
                #     print("found")
            else:
                complete = False
                break
    i = i + 1
    # time.sleep(1)
#
print("startingTestVal {}".format(startTestVal))
