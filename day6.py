from collections import Counter


test = "testInput/"
real = "input/"
day = "day6.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    a = [int(v) for v in a[0].split(',')]
    for i in range(80):
        tot = len(a)
        for j in range(tot):
            if a[j] == 0:
                a[j] = 6
                a.append(8)
            else:
                a[j]-=1
    return len(a)

def part2(a):
    a = [int(v) for v in a[0].split(',')]
    c = Counter(a)
    for i in range(256):
        keys = sorted([key for key in c.keys() if c[key] != 0])
        for v in keys:
            c[v-1] = c[v]
            c[v] = 0
        if c[-1] != 0:
            c[8] = c[-1]
            c[6] += c[-1]
            c[-1] = 0
    return sum(c.values())

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))