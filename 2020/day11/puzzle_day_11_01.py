filepath = 'test'
rows = []
marginHigh = 3

# windowLen = 25
# invalidNum = 57195069


with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.split("\n")
       tmpRow = []
       for c in line[0]:
           tmpRow.append(c)
       rows.append(tmpRow)
       line = fp.readline()

complete = False
newRows = []
while complete == False:
    complete = True
    for i in range(len(rows)):
        for ii in range(len(rows[i])):
            print(rows[i][ii])
            
