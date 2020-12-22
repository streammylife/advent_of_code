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
        for z in numbers:
            if (x + y + z == 2020):
                prod = x * y * z
                print("Num1: {} Num2: {} Num3: {}".format(x, y, z))
                print("Num1 * Num2 * Num3: {}".format(prod))
                complete = True
                break
        if (complete == True):
            break
    if (complete == True):
        break
