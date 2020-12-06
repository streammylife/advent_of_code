filepath = 'input06'

evalLine = ""
uniqueQ = ""
uniqueQTot = 0

groupList = []
searchList = []

groupTot = 0

groupUniqueString = ""
tmpGroupUniqueString = ""
groupInit = False

with open(filepath) as fp:
   line = fp.readline()

   while line:

       if(line.isspace()):
           print(len(groupUniqueString))
           uniqueQTot += len(groupUniqueString)
           groupUniqueString = ""
           groupInit = False
       else:
           if groupInit == False:
               groupInit = True
               for c in line:
                   if c.isalpha():
                       groupUniqueString += c
               print(groupUniqueString)
           else:
               tmpGroupUniqueString = ""
               for c in groupUniqueString:
                   if c in line:
                       tmpGroupUniqueString += c
               groupUniqueString = tmpGroupUniqueString


       groupTot = 0
       line = fp.readline()

print(uniqueQTot)
