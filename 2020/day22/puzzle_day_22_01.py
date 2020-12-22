filepath = 'input'
numbers = []

players = {}


newKeyFound = False

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   player = []
   while line:

       if newKeyFound == False:
           newKeyFound = True
           key = line.split(':')[0]
           players[key] = []
           player = players.get(key)
       else:
           if line.isspace():
               newKeyFound = False
           else:
               player.append(int(line))



       line = fp.readline()

gameOver = False
player1 = players.get("Player 1")
player2 = players.get("Player 2")
while gameOver == False:
    if len(player1) == 0 or len(player2) == 0:
        gameOver = True
    else:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1.extend([p1,p2])
        else:
            player2.extend([p2,p1])

if len(player1) > 0:
    playerToCnt = player1
else:
    playerToCnt = player2

sum = 0
total = len(playerToCnt)
for val in playerToCnt:
    sum = sum + (val * total)
    total = total - 1


print(sum)

print(players)