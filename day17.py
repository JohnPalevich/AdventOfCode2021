from collections import Counter

test = "testInput/"
real = "input/"
day = "day17.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def moveProbe(probeXpos, probeYpos, probeXvel, probeYvel):
    probeXpos += probeXvel
    probeYpos += probeYvel
    probeXvel -= 1 if probeXvel > 0 else 0
    probeYvel -= 1
    return probeXpos, probeYpos, probeXvel, probeYvel

def part1(a):
    info = a[0].split(' ')
    xinfo = [int(v) for v in info[2][2:-1].split('..')]
    yinfo = [int(v) for v in info[3][2:].split('..')]
    leftX = min(xinfo)
    rightX = max(xinfo)
    upY = max(yinfo)
    downY = min(yinfo)

    # print(leftX,rightX)
    # print(upY,downY)
    probeXpos = 0
    probeYpos = 0
    probeXvel = 0
    probeYvel = 0
    steps = []
    for i in range(1, leftX):
        probeXpos = 0 
        probeXvel = i
        step = 0
        while probeXvel !=0:
            probeXpos, probeYpos, probeXvel, probeYvel = moveProbe(probeXpos, probeYpos, probeXvel, probeYvel)
            step += 1
            if leftX <probeXpos < rightX:
                steps.append((step, i))
    #print(steps)
    maxY = 0
    bestXVel = 0
    bestYVel = 0
    for step in steps:
        for i in range(1, abs(downY)):
            bestY = 0
            probeXpos = 0
            probeYpos = 0
            probeXvel = step[1]
            probeYvel = i
            #print('Testing:', probeXvel, probeYvel, end= ' ')
            while probeYpos > downY:
                probeXpos, probeYpos, probeXvel, probeYvel = moveProbe(probeXpos, probeYpos, probeXvel, probeYvel)
                bestY = max(bestY, probeYpos)
            #print('Y Reached:', bestY, end=' ')
            isValid = False
            if leftX <probeXpos < rightX and downY <= probeYpos <= upY:
                if bestY > maxY:
                    maxY = bestY
                    bestXVel = step[1]
                    bestYVel = i
                isValid = True
            #print('Is Valid:', isValid)
    #print(bestXVel, bestYVel)
    return maxY

def part2(a):
    info = a[0].split(' ')
    xinfo = [int(v) for v in info[2][2:-1].split('..')]
    yinfo = [int(v) for v in info[3][2:].split('..')]
    leftX = min(xinfo)
    rightX = max(xinfo)
    upY = max(yinfo)
    downY = min(yinfo)

    # print(leftX,rightX)
    # print(upY,downY)
    probeXpos = probeYpos = probeXvel = probeYvel = 0
    possibleYVelocities = Counter()
    validOnes = []
    for i in range(downY, abs(downY)+1):
        probeYpos = 0
        probeYvel = i
        step = 0
        while probeYpos >= downY:
            probeXpos, probeYpos, probeXvel, probeYvel = moveProbe(probeXpos, probeYpos, probeXvel, probeYvel)
            step += 1
            if downY <= probeYpos <= upY:
                possibleYVelocities[i] += 1

    #print(sorted(possibleYVelocities.keys()), end='\n\n')
    for yVelocity in possibleYVelocities.keys():
        for xVelocity in range(0, rightX+1):
            probeXpos = probeYpos = 0
            probeYpos = 0
            probeXvel = xVelocity
            probeYvel = yVelocity
            #print('Testing:', probeXvel, probeYvel, end= '\n')
            while probeXpos <= rightX and probeYpos >= downY:
                probeXpos, probeYpos, probeXvel, probeYvel = moveProbe(probeXpos, probeYpos, probeXvel, probeYvel)
                if leftX <= probeXpos <= rightX and downY <= probeYpos <= upY:
                    validOnes.append((xVelocity, yVelocity))
    valid = Counter(validOnes)
    #print(sorted(valid))
    return len(valid)


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))