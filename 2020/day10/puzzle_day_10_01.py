filepath = 'test'
numbers = []
window = []
windowLen = 5
invalidNum = 127

# windowLen = 25
# invalidNum = 57195069
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       number = int(line)

       if len(window) < windowLen:
           window.append(number)
       else:
           numbers.append(number)

       line = fp.readline()

   for x in numbers:
       print(window)
       valid = False
       for w1 in window:
           for w2 in window:
               if w1 != w2:
                   if (w1 + w2) == x:
                       valid = True
       if valid == False:
           print("Invalid Num: {}".format(x))
           break
       else:
           window.pop(0)
           window.append(x)
