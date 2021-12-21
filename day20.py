from collections import Counter

test = "testInput/"
real = "input/"
day = "day20.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def enhanceBoard(grid, enhance, default):
    nearby = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0),(1,1)]
    ngrid = [['.' for i in range(len(grid))] for j in range(len(grid[0]))]
    d = {'#':'1', '.':'0'}
    nDefault = enhance[0 if default == '.' else -1]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            binstr = ''
            for n in nearby:
                if 0 <= i+n[0] < len(grid)  and 0 <= j+n[1] < len(grid[0]):
                    binstr += '0' if grid[i+n[0]][j+n[1]] == '.' else '1'
                else:
                    binstr += d[default]
            decimal = int(binstr,2)
            ngrid[i][j] = enhance[decimal]
    for i in range(len(ngrid)):
        ngrid[i] = ''.join(ngrid[i])
    return ngrid, nDefault

def expandBoard(grid, default):
    ngrid = [['.' for i in range(len(grid)+2)] for j in range(len(grid[0])+2)]
    for i in range(len(ngrid)):
        for j in range(len(ngrid[0])):
            if 1 <= i < len(ngrid)-1 and 1 <= j < len(ngrid)-1:
                ngrid[i][j] = grid[i-1][j-1]
            else:
                ngrid[i][j] = default

    for i in range(len(ngrid)):
        ngrid[i] = ''.join(ngrid[i])
    return ngrid



def part1(a):
    enhance = a[0]
    grid = a[2:]
    default = '.'
    for b in range(2):
        grid = expandBoard(grid, default)
        grid, default = enhanceBoard(grid,enhance,default)

    c = Counter()
    for l in grid:
        c.update(l)

    return c['#']

def part2(a):
    enhance = a[0]
    grid = a[2:]
    default = '.'
    for b in range(50):
        grid = expandBoard(grid, default)
        grid, default = enhanceBoard(grid,enhance,default)
    c = Counter()
    for l in grid:
        c.update(l)

    return c['#']


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))