import re

filepath = 'input02'
passwords = []
validPasswords = 0

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       passwords.append(line)
       line = fp.readline()




complete = False

for pw in passwords:
    pwSearch = re.split('-| |: |\n', pw)
    print(pwSearch)
    minNum = int(pwSearch[0])
    maxNum = int(pwSearch[1])
    char = pwSearch[2]
    pwToCheck = pwSearch[3]
    checkIdx = 0
    charCnts = 0
#    print(pwToCheck)
#    print(pwSearch)
#    print(char)
    while checkIdx >= 0:
        checkIdx = pwToCheck.find(char, checkIdx)
#        print(checkIdx)
        if checkIdx >= 0:
            charCnts += 1
            checkIdx += 1
    if charCnts >= minNum and charCnts <= maxNum:
        validPasswords += 1

print(validPasswords)

#print(re.split('-| |: ', passwords[0]))

#for pw in passwords:
#    print(re.split('- | |: ', pw))
