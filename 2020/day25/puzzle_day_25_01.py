import time

start_time = time.time()
filepath = 'input'

cardKey = 11404017
doorKey = 13768789
# cardKey = 5764801
# doorKey = 17807724


startVal = 1
subjectNum = 7


def transform(val, sn):
    val = val * sn
    val = val % 20201227
    return val

complete = False
loop = 0
while complete == False:
    loop = loop + 1
    startVal = transform(startVal, subjectNum)
    if startVal == doorKey:
        complete = True


startVal = 1
subjectNum = cardKey
for i in range(loop):
    startVal = transform(startVal,subjectNum)


print(startVal)




print("--- %s seconds ---" % (time.time() - start_time))