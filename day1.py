test = "testInput/"
real = "input/"
day = "day1.txt"
def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    return a

def part1(a):
    prev = int(a[0])
    tot = 0
    for l in a[1:]:
        if int(l) > prev:
            tot+=1
        prev = int(l)
    return tot

def part2(a):
    prev = -1
    tot = -1
    for i in range(2, len(a)):
        s = sum([int(v) for v in a[i-3:i]])
        tot = tot+1 if s > prev else tot
        prev = s
    return tot

print(part1(getInput(real + day)))
print(part2(getInput(real + day)))