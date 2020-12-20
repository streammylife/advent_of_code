import time
start_time = time.time()

filepath = 'input2'

state = 0
nextState = 0
rules = {}

recursiveCnt = 0

inputs = {}

def checkRule(checkString, rules, ruleToCheck):
    # print("checkRule->checkString: {}".format(checkString))

    global recursiveCnt

    ruleCheck = [False, checkString]

    if ruleToCheck == '8' or ruleToCheck == '11':
        recursiveCnt = recursiveCnt + 1
        if recursiveCnt > 9:
            return  ruleCheck

    ruleCheck = [False, checkString]
    rule = rules[ruleToCheck]
    tmpCheckString = checkString


    for subRule in rule:
        for subSubRule in subRule:
            ruleCheck[0] = False
            if subSubRule.isdigit():
                ruleCheck = checkRule(tmpCheckString, rules, subSubRule)
                if ruleCheck[0] == False:
                    break
                else:
                    tmpCheckString = ruleCheck[1]
            else:
                ruleCheck[0] = False
                if len(tmpCheckString) > 0:
                    if tmpCheckString[0] == subSubRule:
                        ruleCheck[0] = True
                        tmpCheckString = tmpCheckString[1:]
                if ruleCheck[0] == False:
                    break

                # pos = tmpCheckString.find(subSubRule)
                # if pos > -1:
                #     ruleCheck[0] = True
                #     tmpCheckString = checkString[pos+1:]
                # else:
                #     ruleCheck[0] = False
                #     break


        if ruleCheck[0] == True:
            ruleCheck[1] = tmpCheckString
            break
        else:
            tmpCheckString = checkString

    return ruleCheck




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
                subrules = rule[1].replace("\"", "").split("|")

                # rule.append(ruleIdx)

                tmpSubRules = []
                for subRule in subrules:
                    subRule = subRule.split()
                    tmpSubRules.append(subRule)
                    #print("subrule {}".format(subRule))

                rules[ruleIdx] = tmpSubRules
                # rule.append(tmpSubRules)

                # print(tmpSubRules)
                #rules.append(rule)
        elif state == 1:
            checkString = line.split("\n")[0]

            inputs[checkString] = False
            # # print("     ")
            # # print("Checkstring: {}".format(checkString))
            # recursiveCnt = 0
            # result = checkRule(checkString, rules, '0')
            # if result[0] == True:
            #     print("Checkstring: {}".format(checkString))
            #     # cnt = cnt + 1
            #     if len(result[1]) == 0:
            #         cnt = cnt + 1
            # print("Checkstring End: {}".format(checkString))
            # print("Checkstring: {}".format(checkString))
            # for rule in rules:
            #     print("New Rule")
            #     for subRule in rule:
            #         print(subRule)

        state = nextState

        line = fp.readline()


for inputKey in inputs.keys():
    if inputs.get(inputKey) == False:
        result = checkRule(inputKey, rules, '0')
        if result[0] == True:
            if len(result[1]) == 0:
                inputs[inputKey] = True
                cnt = cnt + 1

print("Count: {}".format(cnt))


print("Cnt: {}".format(cnt))
print("--- %s seconds ---" % (time.time() - start_time))
