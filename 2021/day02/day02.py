import time

start_time = time.time()
filepath = 'input'

depth = 0
horiz = 0

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.strip('\n').split(' ')

       if line[0] == "forward":
           depth = depth + int(line[1])
       elif line[0] == "down":
           horiz = horiz + int(line[1])
       elif line[0] == "up":
           horiz = horiz - int(line[1])

       line = fp.readline()


print(depth * horiz)
print("--- %s seconds ---" % (time.time() - start_time))