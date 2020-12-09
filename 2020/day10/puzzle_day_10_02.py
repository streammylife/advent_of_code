filepath = 'input'
numbers = []
window = []
tmpSum = 0
idx = 0


#invalidNum = 127
invalidNum = 57195069

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       number = int(line)
       numbers.append(number)
       line = fp.readline()

for n1 in numbers:
    if(n1 < invalidNum):
        window = []
        tmpSum = 0
        tmpSum = n1
        idx = idx + 1
        window.append(n1)
        for n2 in numbers[idx:]:
            #print(n2)
            window.append(n2)
            tmpSum = tmpSum + n2
            if tmpSum == invalidNum:
                print(n1 + n2)
                break
            elif tmpSum > invalidNum:
                break
    if tmpSum == invalidNum:
        break

print(window)
window.sort()
min = window[0]
window.sort(reverse=True)
max = window[0]
print(min + max)
