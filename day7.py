test = "testInput/"
real = "input/"
day = "day7.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    positions = [int(v) for v in a[0].split(',')]
    maxPos = max(positions)
    totFuel = [0] * maxPos
    for pos in positions:
        for nPos in range(maxPos):
            totFuel[nPos] += abs(pos-nPos)
    return min(totFuel)

def part2(a):
    positions = [int(v) for v in a[0].split(',')]
    maxPos = max(positions)
    totFuel = [0] * maxPos
    for pos in positions:
        for nPos in range(maxPos):
            dPos = abs(pos-nPos)
            totFuel[nPos] += dPos*(dPos+1)//2
    return min(totFuel)

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))