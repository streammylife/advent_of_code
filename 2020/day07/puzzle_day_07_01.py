filepath = 'test'
seats = []

tmpSeatId = 0
maxSeatId = 0

evalLine = ""
uniqueQ = ""
uniqueQTot = 0


with open(filepath) as fp:
   line = fp.readline()

   while line:
       if(line.isspace()):
           print(evalLine)
           for c in evalLine:
               if(c.isalpha()):
                   if c not in uniqueQ:
                       uniqueQ += c
           uniqueQTot += len(uniqueQ)
           print(len(uniqueQ))
           evalLine = ""
           uniqueQ = ""

       evalLine += line
       line = fp.readline()

print(uniqueQTot)
