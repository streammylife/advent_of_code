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

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


busMults = []

lcm_offset = []
for busVal in busVals:
    offset = 0
    idxMatch = busVal[0] + busVal[1]
    mult = 1
    for busVal2 in busVals:
        if busVal2[0] == idxMatch:
            lcm = compute_lcm(busVal[1], busVal2[1])
            offset = busVal2[0]
            # mult = lcm - busVal2[0]
            mult = lcm
            lcm_offset.append(offset)
            busMults.append(mult)
            break


print(lcm_offset)
print(busMults)

lcm = 1;
for busMult in busMults:
    lcm = lcm * busMult
    #lcm = compute_lcm(lcm, busMult)

lcm = 21544599353
print(lcm)

complete = False

i = 1
while complete == False:
    complete = True
    startVal = (busMults[0] * i) - lcm_offset[0]
    for ii in range(1,len(busMults)):
        if (startVal + lcm_offset[ii]) % busMults[ii] != 0:
            complete = False
    i = i + 1

print(startVal)


print("-------")
print(busVals)
complete = False
i = 0
while complete == False:
    complete = True
    checkVal = startVal + (lcm * i)
    #print(checkVal)
    #time.sleep(1)

    for busVal in busVals:
        if (checkVal + busVal[0]) % busVal[1] != 0:
            complete = False
            break
    i = i + 1

print(checkVal)

print("-------")

# complete = False
# lastValidVal = 0
# i = 0
# while complete != True:
#     # print("---------")
#     complete = True
#     startTestVal = int(buses[0]) * i
#     # if (startTestVal + 7) % 133 == 0:
#     #     # print("valid startTestVal: {}".format(startTestVal))
#     #     if (startTestVal + 6) % 155 == 0:
#     #         print("valid startTestVal: {}".format(startTestVal))
#     #         print("valid dif: {}".format(startTestVal - lastValidVal))
#     #         print("-------")
#     #         lastValidVal = startTestVal
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
# #
# print("startingTestVal {}".format(startTestVal))
