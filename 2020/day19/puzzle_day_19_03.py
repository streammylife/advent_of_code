filepath = 'test'

state = 0
nextState = 0
rules = {}
pathStrings = []





with open(filepath) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       if state == 0:
           if line.isspace():
               nextState = state + 1
               print("Rules:")
               for ruleKey in rules.keys():
                   print(rules[ruleKey])
               print("Done with rules")


               path = rules.get('0')[0]
               paths = [path]

               complete = False
               while complete == False:
                   complete = True
                   for i in range(len(paths)):
                       path = paths[i]
                       # print("Path {}".format(path))
                       for ii in range(len(path)):
                           newPathFound = False
                           subPath = path[ii]
                           # print("Subpath {}".format(subPath))
                           if subPath.isdigit():
                               complete = False
                               if len(rules.get(subPath)) > 1:
                                   newPathFound = True
                                   for subRule in rules.get(subPath):
                                       newPath = list(path)
                                       newPath.pop(ii)
                                       for iii in range(len(subRule)):
                                           newPath.insert(iii + ii, subRule[iii])
                                       paths.append(newPath)
                               else:
                                   subRule = rules.get(subPath)[0]
                                   newPath = list(path)
                                   newPath.pop(ii)
                                   for iii in range(len(subRule)):
                                       newPath.insert(iii + ii, subRule[iii])
                                   paths.append(newPath)

                               paths.pop(i)
                               break

                       if complete == False:
                           break
               # print(paths)

               print("Done with paths")


               for path in paths:
                   pathString = "".join(path)
                   pathStrings.append(pathString)

               # print(pathStrings)


           else:
               rule = line.split("\n")[0].split(":")
               ruleIdx = rule[0]
               subrules = rule[1].replace("\"", "").split("|")

               tmpSubRules = []
               for subRule in subrules:
                   subRule = subRule.split()
                   tmpSubRules.append(subRule)

               rules[ruleIdx] = tmpSubRules

       elif state == 1:
           checkString = line.split("\n")[0]
           if checkString in pathStrings:
               cnt = cnt + 1

       state = nextState

       line = fp.readline()

   print("ValidCnt: {}".format(cnt))
