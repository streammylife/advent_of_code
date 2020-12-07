import re
import time
filepath = 'input'
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

def NumOfBagsInsideBag(color):
    numOfBags = 0
    for rule in rules:
        if(color in rule[0]):
            if "no" not in rule[1]:
                print(rule)
                for i in range(1,len(rule)):
                    tmpNumOfBags = int(rule[i][0])
                    tmpColor = rule[i][2:rule[i].find("bag")]
                    print("{} {} Bags Inside".format(tmpNumOfBags, tmpColor))
                    numOfBags += tmpNumOfBags + (tmpNumOfBags * NumOfBagsInsideBag(tmpColor))
    return numOfBags

def IsColorInsideBag(color):
    matchFound = False
    tmpMatches = 0
    for rule in rules:
        if "no" not in rule[1]:
            for i in range(1,len(rule)):
                if MATCH_STRING in rule[i]:
                    color = rule[0][:rule[0].find("bag")]
                    print("Gold Bag Inside This One: {}".format(color))
                    tmpMatches += IsColorInsideBag(color) + 1
                    break
    return tmpMatches

colorsToSearch = ["shiny tomato", "wavy indigo"]
numOfEachColor = [4, 5]
# colorsToSearch = ["dark red", "vibrant plum"]
# numOfEachColor = [2, 2]

totalBags = 0

with open(filepath) as fp:
   line = fp.readline()
   while line:
       tmpRule = line.split("\n")
       tmpRule = tmpRule[0].split(" contain ")
       if MATCH_STRING not in tmpRule[0]:
           rule.append(tmpRule[0])
           tmpRule = tmpRule[1].split(", ")
           for innerBag in tmpRule:
               rule.append(innerBag)
           rules.append(rule)
       rule = []
       line = fp.readline()


totalBags = totalBags + (numOfEachColor[0] + (numOfEachColor[0] * NumOfBagsInsideBag(colorsToSearch[0])))
totalBags = totalBags + (numOfEachColor[1] + (numOfEachColor[1] * NumOfBagsInsideBag(colorsToSearch[1])))

print(totalBags)
