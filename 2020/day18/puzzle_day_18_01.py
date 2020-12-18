filepath = 'test'
numbers = []



def solveEq(eqPieces):

    close = line.find(')')
    while close != -1:
        lastOpen = line.find('(')
        while lastOpen < close
        close = line.find(')')





    newEqStart = line.find('(')
    if newEqStart != -1:
        solveEq(eqPieces)


    operators = ['*', '+']
    opComplete = False
    while(opComplete == False):
        opComplete = True

        for i in range(len(eqPieces)):
            if eqPieces[i].isdigit() == False:
                if(eqPieces[i] == '+'):
                    eqPieces[i] = str(int(eqPieces[i-1]) + int(eqPieces[i+1]))
                else:
                    eqPieces[i] = str(int(eqPieces[i - 1]) * int(eqPieces[i + 1]))
                eqPieces.pop(i + 1)
                eqPieces.pop(i - 1)
                opComplete = False
                break

        # print(opComplete)


        # if any(item in operators for item in eqPieces):
        #     opComplete = False
        #     opIdx = eqPieces.index(operators)
        #     if(eqPieces[opIdx] == '+'):
        #         eqPieces[opIdx] = int(eqPieces[opIdx-1]) + int(eqPieces[opIdx+1])
        #     else:
        #         eqPieces[opIdx] = int(eqPieces[opIdx - 1]) * int(eqPieces[opIdx + 1])
        #     eqPieces.pop(opIdx + 1)
        #     eqPieces.pop(opIdx - 1)

    # multComplete = False
    # while(multComplete == False):
    #     multComplete = True
    #     if '*' in eqPieces:
    #         multComplete = False
    #         multIdx = eqPieces.index('*')
    #         eqPieces[multIdx] = int(eqPieces[multIdx-1]) * int(eqPieces[multIdx+1])
    #         eqPieces.pop(multIdx + 1)
    #         eqPieces.pop(multIdx - 1)
    #
    # addComplete = False
    # while(addComplete == False):
    #     addComplete = True
    #     if '+' in eqPieces:
    #         addComplete = False
    #         multIdx = eqPieces.index('+')
    #         eqPieces[multIdx] = int(eqPieces[multIdx-1]) + int(eqPieces[multIdx+1])
    #         eqPieces.pop(multIdx + 1)
    #         eqPieces.pop(multIdx - 1)

    return int(eqPieces[0])

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   sum = 0
   while line:
       print(line)
       val = solveEq(line.split("\n")[0].split(" "))
       print(val)
       line = fp.readline()

