import time
start_time = time.time()

filepath = 'test'

rules = []

processState = 0
nextState = 0
ticketErrRate = 0
validTickets = []

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:

       # print("Line: {}".format(line))
       if line.isspace():
           processState = processState + 1
           # print("NextState: {}".format(processState))
       else:
           if processState == 0:
               lineItems = line.split()
               lineRule = []
               lineRule.append(lineItems[0])
               print(lineItems)
               for lineItem in lineItems:
                   if(lineItem.find('-') != -1):
                       lineRuleRange = []
                       lineItemRanges = lineItem.split('-')
                       for lineItemRange in lineItemRanges:
                           lineRuleRange.append(int(lineItemRange))
                       lineRule.append(lineRuleRange)
               rules.append(lineRule)

           # if processState == 1:               
           #     if(line.find("ticket") == -1):
           #         ticketNum = line.split("\n")[0]
           #         validTickets.append


           if processState == 2:
               ticketNums = []
               if(line.find("ticket") == -1):
                   #print(line.split("\n")[0].split(','))
                   for ticketNum in line.split("\n")[0].split(','):
                       # ticketNums.append(int(ticketNum))
                       num = int(ticketNum)
                       check = False
                       for rule in rules:
                           if num in range(rule[1][0],rule[1][1] + 1):
                               check = True
                               break
                           elif num in range(rule[2][0],rule[2][1] + 1):
                               check = True
                               break
                       if check == False:
                           print(num)
                           ticketErrRate = ticketErrRate + num




       line = fp.readline()

print("    ")

print(ticketErrRate)

print("--- %s seconds ---" % (time.time() - start_time))




    #
    # newNum = 0
    #
    # if lastNum in prevPrevTurn.keys():
    #     print("prevTurn {}".format(prevTurn[lastNum]))
    #     newNum = prevTurn[lastNum] - prevPrevTurn[lastNum]
    #     prevPrevTurn[lastNum] = prevTurn[lastNum]
    # else:
    #     prevPrevTurn[lastNum] = prevTurn[lastNum]
    #     newNum = 0
    #
    # lastNum = newNum
    # prevTurn[lastNum] = turn
    # turn = turn + 1
    #
