test = "testInput/"
real = "input/"
day = "day2.txt"
def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    return a

def part1(a):
    return

def part2(a):
    return


print(part1(getInput(real + day)))
print(part2(getInput(real + day)))