import time
import re

start_time = time.time()
filepath = 'input'

linesToDecipher = []

knownWordsList = []

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = re.split('\(|\)|contains ', line)
       wordsToDecipher = line[0].split()
       knownWords = line[2].split(', ')
       lineToDecipher = {}
       lineToDecipher["cypher"] = wordsToDecipher
       lineToDecipher["cypherKeys"] = knownWords
       knownWordsList.extend((knownWords))
       linesToDecipher.append(lineToDecipher)
       line = fp.readline()

#remove dupes
knownWordsList = list(dict.fromkeys(knownWordsList))

crackedWords = {}
complete = False
while complete == False:
    complete = True
    newCrackedWords = {}
    for knownWord in knownWordsList:
        matchSet = set()
        firstMatchFound = False
        for ltd in linesToDecipher:
            cypherKeys = ltd.get("cypherKeys")
            if knownWord in cypherKeys:
                if firstMatchFound == False:
                    firstMatchFound = True
                    matchSet = set(ltd.get("cypher"))
                else:
                    matchSet = matchSet & set(ltd.get("cypher"))

                if(len(matchSet) == 1):
                    newCrackedWords[knownWord] = list(matchSet)[0]
                    break;

    if len(newCrackedWords) > 0:
        complete = False
        for key in newCrackedWords.keys():
            newCrackedWord = newCrackedWords.get(key)
            crackedWords[key] = newCrackedWord
            knownWordsList.remove(key)
            for a in linesToDecipher:
                if key in a.get("cypherKeys"):
                    a.get("cypherKeys").remove(key)
                if newCrackedWord in a.get("cypher"):
                    a.get("cypher").remove(newCrackedWord)

print(newCrackedWords)

#
#
#
# crackedWords = {}
# complete = False
# while complete == False:
#     complete = True
#     newCrackedWords = {}
#
#     #crack some words
#     for a in linesToDecipher:
#         cypherKeysA = a.get("cypherKeys")
#         # if len(cypherKeysA) == 1:
#         for b in linesToDecipher:
#             cypherKeysB = b.get("cypherKeys")
#             cypherMatches = set(cypherKeysA) & set(cypherKeysB)
#             if len(cypherMatches) == 1:
#                 matchedCypherKey = cypherKeysA[0]
#                 matches = set(a.get("cypher")) & set(b.get("cypher"))
#                 if len(matches) == 1:
#                     newCrackedWords[matchedCypherKey] = list(matches)[0]
#                     # print(matches)
#
#     #remove cracked words from the list of things to decipher
#     if len(newCrackedWords) > 0:
#         complete = False
#         for key in newCrackedWords.keys():
#             newCrackedWord = newCrackedWords.get(key)
#             crackedWords[key] = newCrackedWord
#             for a in linesToDecipher:
#                 if key in a.get("cypherKeys"):
#                     a.get("cypherKeys").remove(key)
#                 if newCrackedWord in a.get("cypher"):
#                     a.get("cypher").remove(newCrackedWord)
#
#     #count how many ingredients are left

#how many times good ingredients were used
count = 0
for a in linesToDecipher:
    count = count + len(a.get("cypher"))

print(count)

ingString = ""
for key in sorted(crackedWords.keys()):
    ingString = ingString + crackedWords.get(key) + ','

print(ingString)

print(sorted(crackedWords))


print("--- %s seconds ---" % (time.time() - start_time))