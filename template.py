test = "testInput/"
real = "input/"
day = "day.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    return

def part2(a):
    return


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
#print(part2(testInput))
#print(part2(input))