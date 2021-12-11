import heapq

test = "testInput/"
real = "input/"
day = "day11.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a


adjacent= [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]

def part1(a):
    a = [[(int(v),False) for v in l] for l in a]
    flashes = 0
    needToFlash = set()
    
    def update(row, col):
        for loc in adjacent:
            nRow = row+loc[0]
            nCol = col+loc[1]
            if 0 <= nRow < len(a) and 0<=nCol<len(a[0]):
                if not a[nRow][nCol][1]:
                    a[nRow][nCol] = (a[nRow][nCol][0]+1, False)
                    if a[nRow][nCol][0] > 9:
                        needToFlash.add((nRow,nCol))
        a[row][col] = (0, True)

    for _ in range(100):
        #setup array
        a = [[(int(v[0]),False) for v in l] for l in a]
        needToFlash = set()
        #Update all squids
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = (a[i][j][0]+1, a[i][j][1])
                if a[i][j][0] > 9:
                    update(i, j)
                    flashes+=1
        #Update remaining needToFlash Squids
        while len(needToFlash) > 0:
            location = needToFlash.pop()
            #if not already flashed
            if not a[location[0]][location[1]][1]:
                update(location[0],location[1])
                flashes+=1
    return flashes
        

                    


    return

def part2(a):
    a = [[(int(v),False) for v in l] for l in a]
    needToFlash = set()

    def update(row, col):
        for loc in adjacent:
            nRow = row+loc[0]
            nCol = col+loc[1]
            if 0 <= nRow < len(a) and 0<=nCol<len(a[0]):
                if not a[nRow][nCol][1]:
                    a[nRow][nCol] = (a[nRow][nCol][0]+1, False)
                    if a[nRow][nCol][0] > 9:
                        needToFlash.add((nRow,nCol))
        a[row][col] = (0, True)

    flashes = 0
    step = 0
    while flashes != 100:
        #Reset flashed
        flashes = 0
        a = [[(int(v[0]),False) for v in l] for l in a]
        needToFlash = set()
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = (a[i][j][0]+1, a[i][j][1])
                if a[i][j][0] > 9:
                    update(i, j)
                    flashes+=1
        while len(needToFlash) > 0:
            location = needToFlash.pop()
            if not a[location[0]][location[1]][1]:
                update(location[0],location[1])
                flashes+=1
        step+=1
    return step


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))