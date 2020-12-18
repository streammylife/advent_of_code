import time
start_time = time.time()

filepath = 'input'
numbers = []



def parsePars(line):
    close = line.find(')')
    while close != -1:
        # print(line)
        open = line.rfind('(', 0, close)
        # print(line)
        val = solveEq(line[open+1:close].split(" "))
        # print("val {}".format(val))
        line = line[:open] + str(val) + line[close+1:]
        # print("new line {}".format(line))
        close = line.find(')')
        # print("close {}".format(close))
        # time.sleep(3)
    # print(line)
    # print(solveEq(line.split(" ")))
    return(solveEq(line.split(" ")))


def solveEq(eqPieces):
    addComplete = False
    while(addComplete == False):
        addComplete = True
        if '+' in eqPieces:
            addComplete = False
            multIdx = eqPieces.index('+')
            eqPieces[multIdx] = int(eqPieces[multIdx-1]) + int(eqPieces[multIdx+1])
            eqPieces.pop(multIdx + 1)
            eqPieces.pop(multIdx - 1)

    multComplete = False
    while(multComplete == False):
        multComplete = True
        if '*' in eqPieces:
            multComplete = False
            multIdx = eqPieces.index('*')
            eqPieces[multIdx] = int(eqPieces[multIdx-1]) * int(eqPieces[multIdx+1])
            eqPieces.pop(multIdx + 1)
            eqPieces.pop(multIdx - 1)



    return int(eqPieces[0])

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   sum = 0
   while line:
       # print(line)
       val = parsePars(line.split("\n")[0])
       sum = sum + val
       # print(val)
       line = fp.readline()

print("Sum: {}".format(sum))


print("--- %s seconds ---" % (time.time() - start_time))
