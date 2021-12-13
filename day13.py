test = "testInput/"
real = "input/"
day = "day13.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def print_grid(a, max_x, max_y):
    for l in a[:max_y]:
        s = ''
        for c in l[:max_x]:
            s+= '#' if c else '.'
        print(s)
    return 

def fold(grid, axis, num, max_x, max_y):
    if axis == 'x':
        for col in range(num, max_x+1):
            for row in range(max_y+1):
                if grid[row][col]:
                    grid[row][col] = False
                    grid[row][col-2*abs(num-col)] = True
        max_x = num
    else:
        for col in range(max_x+1):
            for row in range(num, max_y+1):
                if grid[row][col]:
                    grid[row][col] = False
                    grid[row-2*abs(num-row)][col] = True
        max_y = num
    return max_x, max_y, grid

def part1(a):
    totCoords = []
    i = max_x = max_y = 0
    while a[i] != '':
        coords = a[i].split(',')
        totCoords.append((int(coords[0]),int(coords[1])))
        max_x = max(max_x, int(coords[0]))
        max_y = max(max_y, int(coords[1]))
        i+=1
    grid = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]
    
    for coord in totCoords:
        grid[coord[1]][coord[0]] = True
    i += 1

    info = a[i].split('=')
    axis = info[0][-1]
    num = int(info[1])
    _, _, grid = fold(grid, axis, num, max_x, max_y)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                count+=1

    return  count

def part2(a):
    i = 0
    totCoords = []
    max_x = 0
    max_y = 0
    while a[i] != '':
        coords = a[i].split(',')
        totCoords.append((int(coords[0]),int(coords[1])))
        max_x = max(max_x, int(coords[0]))
        max_y = max(max_y, int(coords[1]))
        i+=1
    grid = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]
    
    for coord in totCoords:
        grid[coord[1]][coord[0]] = True
    i +=1

    while i < len(a):
        info = a[i].split('=')
        axis = info[0][-1]
        num = int(info[1])
        max_x, max_y, grid = fold(grid, axis, num, max_x, max_y)
        i+=1
    count = 0
    print_grid(grid,max_x,max_y)
    return 


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
#print(part2(testInput))
print(part2(input))