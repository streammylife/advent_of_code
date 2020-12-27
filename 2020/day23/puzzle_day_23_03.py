import time

start_time = time.time()
filepath = 'input'

# input = "389125467"
input = "469217538"
numberOfRounds = 10000000
numberOfCards = 1000000

cups = []
cards = {}


inputLen = len(input)
for i in range(inputLen):
    cards[int(input[i])] = int(input[(i + 1) % inputLen])

for i in range(10,numberOfCards + 1):
    cards[i] = i + 1
    # print(i)

cards[8] = 10
cards[numberOfCards] = 4;

sel = 4
comp = 0
for i in range(numberOfRounds):
    # tmpTime = time.time()

    if i % 1000000 == 0:
        print("{}% Complete".format(comp))
        comp = comp + 10

    pickup1 = cards.get(sel)
    pickup2 = cards.get(pickup1)
    pickup3 = cards.get(pickup2)

    next = cards.get(pickup3)

    dest = (sel - 1)
    if dest == 0:
        dest = numberOfCards
    while dest in [pickup1,pickup2,pickup3]:
        dest = (dest - 1)
        if dest == 0:
            dest = numberOfCards

    cards[pickup3] = cards[dest]
    cards[dest] = pickup1
    cards[sel] = next
    sel = next

    # print("--- %s seconds ---" % (time.time() - tmpTime))



# tmpDest = cards.get(1)
# for i in range(numberOfCards - 1):
#     print(tmpDest)
#     tmpDest = cards.get(tmpDest)



cup1 = cards.get(1)
cup2 = cards.get(cup1)
mult = cup1 * cup2

print(mult)

print("--- %s seconds ---" % (time.time() - start_time))