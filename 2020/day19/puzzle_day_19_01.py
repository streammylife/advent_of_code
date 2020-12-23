import time
start_time = time.time()

filepath = 'input'

state = 0
nextState = 0
rules = {}

recursiveCheck = 0

def checkRule(checkString, rules, ruleToCheck):

    global recursiveCheck

    # print("checkRule->checkString: {}".format(checkString))
    ruleCheck = [False, checkString]


    rule = rules[ruleToCheck]
    tmpCheckString = checkString
    for subRule in rule:
        for subSubRule in subRule:
            ruleCheck[0] = False
            if subSubRule.isdigit():

                # if recursiveCheck  > 50:
                #     ruleCheck = [False, checkString]
                #     return ruleCheck
                #
                # if subSubRule == "42" or subSubRule == '31':
                #     # print("Checking rule: {}".format(subSubRule))
                #     recursiveCheck = recursiveCheck + 1

                ruleCheck = checkRule(tmpCheckString, rules, subSubRule)


                if ruleCheck[0] == False:
                    break
                else:
                    tmpCheckString = ruleCheck[1]
            else:

                if len(tmpCheckString) > 0:
                    if tmpCheckString[0] == subSubRule:
                        ruleCheck[0] = True
                        tmpCheckString = tmpCheckString[1:]
                    else:
                        ruleCheck[0] = False
                        break
                else:
                    ruleCheck[0] = False
                    break
        if ruleCheck[0] == True:
            ruleCheck[1] = tmpCheckString
            break
        else:
            tmpCheckString = checkString

    return ruleCheck


checkStrings = []

with open(filepath) as fp:
    line = fp.readline()
    cnt = 0
    while line:
        if state == 0:
            if line.isspace():
                nextState = state + 1
                print("Rules:")
                print(rules)
                print("Done with rules")
            else:
                rule = line.split("\n")[0].split(":")
                ruleIdx = rule[0]
                subrules = rule[1].replace("\"","").split("|")


                tmpSubRules = []
                for subRule in subrules:
                    subRule = subRule.split()
                    tmpSubRules.append(subRule)

                rules[ruleIdx] = tmpSubRules

                print(tmpSubRules)
        elif state == 1:
            checkString = line.split("\n")[0]
            checkStrings.append(checkString)

        state = nextState

        line = fp.readline()


matchStrings = []

newMatchStrings = []


base8 = ['42']
base11 = ['42','31']
base = ['42','42','31']

tmpRule = []
tmpRule.append([['42','42','31']])

complete = False
doneFlag = False
loopCnt = 0
while complete == False:
    tmpRule = []
    tmpRule.append([base])
    # print(tmpRule)
    newCnt = 0
    # for i in range(len(tmpRule)):
    rules['0'] = tmpRule[0]

    newMatchStrings = []
    for checkString in checkStrings:
        recursiveCheck = 0
        # print("     ")
        # print("Checkstring: {}".format(checkString))
        result = checkRule(checkString, rules, '0')
        if result[0] == True:
            if len(result[1]) == 0:
                newCnt = newCnt + 1
                newMatchStrings.append(checkString)

    for newMatchString in newMatchStrings:
        matchStrings.append(newMatchString)
        checkStrings.remove(newMatchString)





    # complete = True

    if loopCnt < 10:
        loopCnt = loopCnt + 1
        cnt = cnt + newCnt
        newCnt = 0
        doneFlag = False
        base.insert(0,'42')
    # if newCnt > 0:
    #     cnt = cnt + newCnt
    #     newCnt = 0
    #     doneFlag = False
    #     base.insert(0,'42')
    else:
        loopCnt = 0
        # if doneFlag == True:
        #     complete = True
        # else:
        #     doneFlag = True
        base11.insert(0,'42')
        base11.append('31')
        base = []
        base.append('42')
        base.extend(base11)
        print(base)










print("Cnt: {}".format(cnt))
print("--- %s seconds ---" % (time.time() - start_time))
