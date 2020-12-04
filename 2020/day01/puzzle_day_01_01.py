filepath = 'input01'
numbers = []
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       numbers.append(int(line))
       line = fp.readline()

print("Numbers Count: {}".format(len(numbers)))

complete = False

for x in numbers:
    for y in numbers:
        if (x + y == 2020):
            z = x * y
            print("Num1: {} Num2: {}".format(x, y))
            print("Num1 * Num2: {}".format(z))
            complete = True
            break
    if (complete == True):
        break
