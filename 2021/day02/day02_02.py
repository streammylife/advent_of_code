import time

start_time = time.time()
filepath = 'input'

depth = 0
horiz = 0
aim = 0

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.strip('\n').split(' ')
       com = line[0]
       val = int(line[1])

       if com == "forward":
           horiz = horiz + val
           depth = depth + (aim * val)
       elif com == "down":
           aim = aim + val
       elif com == "up":
           aim = aim - val

       line = fp.readline()


print(depth * horiz)
print("--- %s seconds ---" % (time.time() - start_time))