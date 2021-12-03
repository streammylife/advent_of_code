import time

start_time = time.time()
filepath = 'input'

gamma = 0
eps = 0

oneCnt = [0] * 12
zeroCnt = [0] * 12


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       for i in range(12):
           if line[i] == '0':
               zeroCnt[i] = zeroCnt[i] + 1
           elif line[i] == '1':
               oneCnt[i] = oneCnt[i] + 1
       line = fp.readline()


for ii in range(12):
    if oneCnt[ii] > zeroCnt[ii]:
        gamma = gamma | (1 << (11-ii))
    else:
        eps = eps | (1 << (11-ii))

power = eps * gamma

print("--- %s seconds ---" % (time.time() - start_time))