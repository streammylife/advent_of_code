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
    pos1 = int(pwSearch[0]) - 1
    pos2 = int(pwSearch[1]) - 1
    char = pwSearch[2]
    pwToCheck = pwSearch[3]
    checkIdx = 0
    charCnts = 0

#    print(char)
#    print(pwToCheck.find(char, pos1, pos1))
    if pwToCheck.find(char, pos1, pos1+1) >= 0:
        charCnts += 1

    if pwToCheck.find(char, pos2, pos2+1) >= 0:
        charCnts += 1

    print(charCnts)

    if(charCnts == 1):
        validPasswords += 1

print(validPasswords)

#print(re.split('-| |: ', passwords[0]))

#for pw in passwords:
#    print(re.split('- | |: ', pw))
