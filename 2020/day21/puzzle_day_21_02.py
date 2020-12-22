import time

start_time = time.time()

filepath = 'input'
numbers = []

players = {}

PLAYER1_KEY = "Player 1"
PLAYER2_KEY = "Player 2"

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


def calcPlayerHash(playerToCnt):
    sum = 0
    total = len(playerToCnt)
    for val in playerToCnt:
        sum = sum + (val * total)
        total = total - 1
    return sum

def calcRoundHash(players):
    global PLAYER1_KEY
    global PLAYER2_KEY
    hash1 = calcPlayerHash(players.get(PLAYER1_KEY))
    hash2 = calcPlayerHash(players.get(PLAYER2_KEY))

    return (hash1 * 13) * hash2 + 5


def playTheGame(players):
    # players = gamePlayers.copy()
    gameRoundHashes = []
    gameOver = False
    player1 = players.get("Player 1")
    player2 = players.get("Player 2")
    while gameOver == False:
        if len(player1) == 0 or len(player2) == 0:
            if len(player1) > 0:
                winner = PLAYER1_KEY
            else:
                winner = PLAYER2_KEY
            gameOver = True
        else:
            roundHash = calcRoundHash(players)
            if roundHash in gameRoundHashes:
                winner = PLAYER1_KEY
                gameOver = True
            else:
                p1 = player1.pop(0)
                p2 = player2.pop(0)

                if p1 > len(player1) or p2 > len(player2):
                    if p1 > p2:
                        player1.extend([p1,p2])
                    else:
                        player2.extend([p2,p1])
                else:
                    subPlayers = {}
                    subPlayers[PLAYER1_KEY] = player1[:p1]
                    subPlayers[PLAYER2_KEY] = player2[:p2]
                    subWinner = playTheGame(subPlayers)
                    if subWinner == PLAYER1_KEY:
                        player1.extend([p1,p2])
                    else:
                        player2.extend([p2,p1])




                gameRoundHashes.append(roundHash)


    return winner


winner = playTheGame(players)

winnerDeck = players[winner]

winnerHash = calcPlayerHash((winnerDeck))

print(winnerHash)

print(players)


print("--- %s seconds ---" % (time.time() - start_time))