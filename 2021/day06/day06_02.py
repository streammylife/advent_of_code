import time

start_time = time.time()
filepath = 'input'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = fp.readline()

print("--- %s seconds ---" % (time.time() - start_time))