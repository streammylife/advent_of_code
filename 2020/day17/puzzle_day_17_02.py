import time
start_time = time.time()

filepath = 'input'

rules = {}

processState = 0
nextState = 0
ticketErrRate = 0
validTickets = []

myTicket = []

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:

       # #print("Line: {}".format(line))
       if line.isspace():
           processState = processState + 1
           # #print("NextState: {}".format(processState))
       else:
           if processState == 0:
               lineItems = line.split(':')
               lineRule = []
               lineRuleKey = lineItems[0]
               lineItems = lineItems[1].split()
               for lineItem in lineItems:
                   if(lineItem.find('-') != -1):
                       lineRuleRange = []
                       lineItemRanges = lineItem.split('-')
                       for lineItemRange in lineItemRanges:
                           lineRuleRange.append(int(lineItemRange))
                       lineRule.append(lineRuleRange)
               rules[lineRuleKey] = lineRule

           if processState == 1:
               if(line.find("ticket") == -1):
                   ticket = line.split("\n")[0]
                   for s in ticket.split(','):
                       myTicket.append(int(s))


           if processState == 2:
               ticketNums = []
               if(line.find("ticket") == -1):
                   ##print(line.split("\n")[0].split(','))
                   ticket = line.split("\n")[0]
                   isValid = True
                   for ticketNum in ticket.split(','):
                       # ticketNums.append(int(ticketNum))
                       num = int(ticketNum)
                       check = False
                       for key in rules:
                           rule = rules[key]
                           if num in range(rule[0][0],rule[0][1] + 1):
                               check = True
                               break
                           elif num in range(rule[1][0],rule[1][1] + 1):
                               check = True
                               break
                       if check == False:
                           #print(num)
                           ticketErrRate = ticketErrRate + num
                           isValid = False
                           break
                   if isValid == True:
                       nums = []
                       for s in ticket.split(','):
                           nums.append(int(s))
                       validTickets.append(nums)
       line = fp.readline()

missingRules = {}
foundRules = {}
for i in range(len(rules)):
    missingRules[i] = i

#print(missingRules)

def IsNumInRule(num, rule):
    result = False
    #print(num)
    #print(type(num))
    #print(rule)
    if num in range(rule[0][0],rule[0][1] + 1):
        result = True
        #print("sdfs")
    elif num in range(rule[1][0],rule[1][1] + 1):
        result = True
        #print("sdfs")
    return result


print("Valid Tickets: {}".format(len(validTickets)))

complete = False
while complete == False:
    # print("   ")
    # print("Next Loop")
    # print("--------")
    # print("Rules: {}".format(rules.keys()))
    # print("Positions Left: {}".format(missingRules.keys()))
    complete = True
    for key in missingRules.keys():
        #print("Missing Rule Key {}".format(key))
        ruleMatches = {}
        for ruleKey in rules.keys():
            check = False
            for validTic in validTickets:
                #print("validTic {}".format(validTic))
                valToCheck = validTic[key]
                #print("valToCheck: {}".format(valToCheck))
                #print("Rule to check: {}".format(rules[ruleKey]))
                check = IsNumInRule(valToCheck, rules[ruleKey])
                #print("Rule check result: {}".format(check))
                if check == False:
                    break
            if check == True:
                ruleMatches[ruleKey] = key

        numOfRuleMatches = len(ruleMatches)
        if(numOfRuleMatches) == 1:
            complete = False
            tmpKey = ruleMatches.keys()[0]
            foundRules[tmpKey] = ruleMatches[tmpKey]
            break
        # elif(numOfRuleMatches == 2):
        #     print(rules[ruleKey])
        #     print(ruleMatches)
    if complete == False:
        missingRules.pop(ruleMatches[tmpKey])
        rules.pop(tmpKey)

print("Found Rules: {}".format(foundRules))
print("My Ticket: {}".format(myTicket))

depProd = 1
for key in foundRules.keys():
    if key.find("departure") != -1:
        print(foundRules[key])
        depProd = depProd * myTicket[foundRules[key]]

print("depProd: {}".format(depProd))














# #print("    ")
#
print("Ticket Error Rate: {}".format(ticketErrRate))
# #print("Valid Tickets:")
# for validTic in validTickets:
#     #print(validTic)

print("--- %s seconds ---" % (time.time() - start_time))




    #
    # newNum = 0
    #
    # if lastNum in prevPrevTurn.keys():
    #     #print("prevTurn {}".format(prevTurn[lastNum]))
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
