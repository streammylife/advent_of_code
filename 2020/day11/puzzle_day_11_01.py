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

adapters.sort()
#print(adapters[0] + marginHigh)
#print(adapters)

oneJGaps = 0
threeJGaps = 0
startJ = 0

lastVal = startJ
for a in adapters:
    dif = a - lastVal
    if dif == 1:
        oneJGaps = oneJGaps + 1
    elif dif == 3:
        threeJGaps = threeJGaps + 1
    lastVal = a

#to get to max
threeJGaps = threeJGaps + 1


print(oneJGaps)
print(threeJGaps)
print(oneJGaps * threeJGaps)


# for a in adapters:
#     print(a)

   # print(window)
   # valid = False
   # for w1 in window:
   #     for w2 in window:
   #         if w1 != w2:
   #             if (w1 + w2) == x:
   #                 valid = True
   # if valid == False:
   #     print("Invalid Num: {}".format(x))
   #     break
   # else:
   #     window.pop(0)
   #     window.append(x)
