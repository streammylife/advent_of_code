import re
filepath = 'test'
seats = []

tmpSeatId = 0
maxSeatId = 0

evalLine = ""
uniqueQ = ""
uniqueQTot = 0

rules = []
rule = []

matches = 0

MATCH_STRING = "shiny gold"

deadEndColors = []

def IsGoldBagInside(color):
    matchFound = False
    if color not in deadEndColors:
        print("----Color to search: {}".format(color))
        for rule in rules:
            if color in rule[0]:
                if "no " not in rule[1]:
                    for i in range(1,len(rule)):
                        if MATCH_STRING in rule[i]:
                            matchFound = True
                            break
                        else:
                            color = rule[i][2:rule[i].find("bag")]
                            matchFound = IsGoldBagInside(color)
                    if matchFound:
                        break
    return matchFound





with open(filepath) as fp:
   line = fp.readline()
   while line:
       tmpRule = line.split("\n")
       tmpRule = tmpRule[0].split(" contain ")
       rule.append(tmpRule[0])
       tmpRule = tmpRule[1].split(", ")
       for innerBag in tmpRule:
           rule.append(innerBag)
       rules.append(rule)
       rule = []
       line = fp.readline()

   for rule in rules:
       print("Rule to search: {}".format(rule))
       matchFound = False
       if MATCH_STRING not in rule[0]:
           if "no" not in rule[1]:
               for i in range(1,len(rule)):
                   if MATCH_STRING in rule[i]:
                       # print(rule[i])
                       matchFound = True
                       break
                   else:
                       color = rule[i][2:rule[i].find("bag")]
                       matchFound = IsGoldBagInside(color)
                       if matchFound == False:
                           deadEndColors.append(color)

       if(matchFound):
           matches += 1



print(matches)
