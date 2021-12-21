from collections import Counter
test = "testInput/"
real = "input/"
day = "day21.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    p1 = int(a[0][-1])
    p2 = int(a[1][-1])
    p1score = 0
    p2score = 0
    rounds = 0
    dice = 1
    while p1score < 1000 and p2score < 1000:
        p1movement = 3*dice+3
        dice += 3
        p1 = p1movement+p1
        while p1 > 10:
            p1-=10
        p1score += p1
        rounds +=3
        if p1score >= 1000:
            break
        p2movement = 3*dice+3
        dice += 3
        p2 = p2movement + p2
        while p2> 10:
            p2-=10
        p2score += p2
        rounds += 3
    #print(p1score, p2score, rounds)
    

    return min(p1score,p2score) * rounds

def part2(a):
    p1 = int(a[0][-1])
    p2 = int(a[1][-1])
    gameScores = Counter()
    gameScores[(p1, 0, p2, 0, True)] = 1
    finishedGames = Counter()
    combos = []
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                combos.append((i,j,k))
    print(len(combos))
    while len(gameScores) > 0:
        tempGameScore = Counter()
        for game in gameScores.keys():
            for combo in combos:
                if game[4]:
                    tempP1 = game[0]
                    tempScore = game[1]
                    tempP1 += sum(combo)
                    while tempP1 > 10:
                        tempP1-=10
                    tempScore += tempP1
                    if tempScore >= 21:
                        finishedGames['1'] += gameScores[game]
                    else:
                        newGame = (tempP1, tempScore, game[2], game[3], False)
                        tempGameScore[newGame] += gameScores[game]
                else:
                    tempP2 = game[2]
                    tempScore = game[3]
                    tempP2 += sum(combo)
                    while tempP2 > 10:
                        tempP2 -= 10
                    tempScore += tempP2
                    if tempScore >= 21:
                        finishedGames['2'] += gameScores[game]
                    else:
                        newGame = (game[0], game[1], tempP2, tempScore, True)
                        tempGameScore[newGame] += gameScores[game]
        gameScores = tempGameScore
    # print(finishedGames)
    # print(finishedGames['1'] + finishedGames['2'])
    # print(444356092776315 + 341960390180808)
    return finishedGames.most_common(1)[0][1]


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))