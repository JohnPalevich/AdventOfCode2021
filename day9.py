test = "testInput/"
real = "input/"
day = "day9.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    for i in range(len(a)):
        a[i] = [int(v) for v in a[i]]
    mins = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            curr = a[i][j]
            isMin = True
            if i>=1 and a[i-1][j] <= curr:
                isMin = False
            if j>=1 and a[i][j-1] <= curr:
                isMin = False
            if j < len(a[0])-1 and a[i][j+1] <= curr:
                isMin = False
            if i < len(a)-1 and a[i+1][j] <= curr:
                isMin = False
            mins+= 1 + curr if isMin else 0
    return mins

def part2(a):
    for i in range(len(a)):
        a[i] = [int(v) for v in a[i]]
    sizes = []
    
    seen = [[False for i in range(len(a[0]))] for j in range(len(a))]
    def findBasin(a, row, col):
        if 0 <= row < len(a) and 0<=col<len(a[0]) and a[row][col]!=9 and not seen[row][col]:
            seen[row][col] = True
            return 1 + findBasin(a, row-1, col) + findBasin(a,row,col-1) + findBasin(a, row+1, col) + findBasin(a,row,col+1)
        return 0

    for i in range(len(a)):
        for j in range(len(a[0])):
            curr = a[i][j]
            isMin =  True
            if i>=1 and a[i-1][j] <= curr:
                isMin = False
            if j>=1 and a[i][j-1] <= curr:
                isMin = False
            if j < len(a[0])-1 and a[i][j+1] <= curr:
                isMin = False
            if i < len(a)-1 and a[i+1][j] <= curr:
                isMin = False
            if isMin:
                v = findBasin(a, i, j)
                sizes.append(v)
    sizes = sorted(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))