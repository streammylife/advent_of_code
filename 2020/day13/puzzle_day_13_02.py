import time

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

complete = False
multFact = 1
while complete == False:
    complete = True
    startVal = ((busVals[0][1] * 658) * multFact) + (busVals[0][1] * (multFact-1))
    #startVal = (busVals[0][1]) * multFact
    # print("startVal {}".format(startVal))
    # if((startVal + busVals[0][1]) % 19) == 0:
    #     print("valid startVal: {}".format(startVal))
    # if True:
    for i in range(1,len(busVals)):
        valToCheck = startVal + busVals[i][0]
        if valToCheck % busVals[i][1] != 0:
            complete = False
            break

    # else:
    #     complete = False

    multFact = multFact + 1
    # time.sleep(1)

print(startVal)

# complete = False
# while complete != True:
#     # print("---------")
#     complete = True
#     startTestVal = int(buses[0]) * i
#     for ii in range(1,len(buses)):
#         testVal = startTestVal + ii
#         if(buses[ii] != 'x'):
#             if testVal >= int(buses[ii]):
#                 if (testVal % int(buses[ii])) != 0:
#                     complete = False
#                     break
#                 # else:
#                 #     print("testVal {}".format(testVal))
#                 #     print("number check {}".format(int(buses[ii])))
#                 #     print("found")
#             else:
#                 complete = False
#                 break
#     i = i + 1
#     # time.sleep(1)
#
# print("startingTestVal {}".format(startTestVal))
