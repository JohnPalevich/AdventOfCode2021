test = "testInput/"
real = "input/"
day = "day2.txt"
def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    h = 0
    d = 0
    for l in a:
        l = l.split(' ')
        dir = l[0]
        dist = int(l[1])
        if dir == "forward":
            h += dist
        elif dir == "down":
            d += dist
        elif dir == "up":
            d -= dist
    return d*h

def part2(a):
    h = 0
    d = 0
    aim = 0
    for l in a:
        l = l.split(' ')
        dir = l[0]
        val = int(l[1])
        if dir == "forward":
            h += val
            d += val * aim
        elif dir == "down":
            aim += val
        elif dir == "up":
            aim -= val
    return d*h

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))