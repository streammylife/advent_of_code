import re
import time

filepath = 'input'
pc = 0
operations = []
accumulator = 0
executed = []
switched = []

loopComplete = False

def ClearExecuted():
    for i in range(0,len(executed)):
        executed[i] = False

def RunLoop(operations):
    returnVal = [0,0]
    pc = 0
    loopComplete = False
    accumulator = 0
    ClearExecuted()
    while loopComplete == False:
        if pc == len(operations):
            loopComplete = True
            print(accumulator)
            print("END")
        else:
            if executed[pc] == False:
                #print(operations[pc])
                opType = operations[pc][:3]
                sign = operations[pc][4]
                val = int(operations[pc][5:])
                # print(opType)
                # print(sign)
                # print(val)
                # print("----")

                executed[pc] = True

                if opType == "nop":
                    pc = pc + 1
                elif opType == "acc":
                    pc = pc + 1
                    if sign == "+":
                        accumulator = accumulator + val
                    else:
                        accumulator = accumulator - val
                elif opType == "jmp":
                    if sign == "+":
                        pc = pc + val
                    else:
                        pc = pc - val
            else:
                loopComplete = True

    return pc

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       operations.append(line)
       executed.append(False)
       switched.append(False)
       line = fp.readline()
   for i in range(0,len(executed)):
       oldOperation = operations[i]
       opType = operations[i][:3]
       if opType != "acc":
           # print(opType)
           if opType == "nop":
               newOpType = "jmp"
           elif opType == "jmp":
               newOpType = "nop"
           newOperation = newOpType + operations[i][3:]
           #print(newOperation)
           operations[i] = newOperation
           # print("Starting New")
           # print("----")
           #print(operations)
           testPc = RunLoop(operations)
           if testPc == len(operations):
               break
           else:
               operations[i] = oldOperation




print(accumulator)
