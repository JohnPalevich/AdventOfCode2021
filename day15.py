import heapq

test = "testInput/"
real = "input/"
day = "day15.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    neighbors = [(0,1),(1,0)]
    dist = {}
    prev = {}
    for i in range(len(a)):
        for j in range(len(a[i])):
            dist[(i,j)] = 10000000000000
            prev[(i,j)] = None
    dist[(0,0)] = 0
    fin_dist = {}
    #Djikstra's
    while (i,j) in dist.keys():
        min_key = min(dist, key=dist.get)
        fin_dist[min_key] = dist[min_key]
        dist.pop(min_key)
        for neighbor in neighbors:
            row = min_key[0]+neighbor[0]
            col = min_key[1]+neighbor[1]
            if 0 <= row < len(a) and 0 <= col < len(a[0]):
                nD = fin_dist[(min_key)] + int(a[row][col])
                if (row,col) in dist.keys() and nD < dist[(row,col)]:
                    dist[(row,col)] =  nD
                    prev[(row,col)] = min_key
    reverse = (len(a)-1, len(a[0])-1)
    risk = fin_dist[reverse]
    return risk

def part2(a):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    dist = {}
    prev = {}
    val = {}
    for i in range(1, len(a)+1):
        for j in range(1, len(a[0])+1):
            for k in range(0,5):
                for l in range(0,5):
                    row = i+len(a)*k
                    col = j+len(a[0]*l)
                    dist[(row,col)] = 1000000000
                    v_at_loc = (int(a[i-1][j-1]) + 1*((k)+(l)))%9
                    val[(row, col)] = v_at_loc if v_at_loc !=0 else 9
    dist[(1,1)] = val[(1,1)]
    pq = [(1,1)]
    fin_dist = {}
    #A*
    while len(pq) > 0:
        min_key = heapq.heappop(pq)
        fin_dist[min_key] = dist[min_key]
        for neighbor in neighbors:
            row = min_key[0]+neighbor[0]
            col = min_key[1]+neighbor[1]
            if 0 < row <= len(a)*5 and 0 < col <= len(a[0])*5:
                nD = fin_dist[(min_key)] + val[(row,col)]
                if (row,col) in dist.keys() and nD < dist[(row,col)]:
                    dist[(row,col)] =  nD
                    prev[(row,col)] = min_key
                    heapq.heappush(pq, (row,col))
    reverse = (len(a)*5, len(a[0])*5)
    #print(fin_dist)
    risk = fin_dist[reverse]-fin_dist[(1,1)]
    return risk


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
#print(part1(input))
print(part2(testInput))
print(part2(input))