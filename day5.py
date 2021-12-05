from collections import Counter
test = "testInput/"
real = "input/"
day = "day5.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    c = Counter()
    for line in a:
        coords = line.split('->')
        initPos = coords[0].strip(' ').split(',')
        x1 = int(initPos[0])
        y1 = int(initPos[1])
        destPos = coords[1].strip(' ').split(',')
        x2 = int(destPos[0])
        y2 = int(destPos[1])
        if x2 == x1:
            for i in range(min(y1,y2), max(y1, y2)+1):
                c[(x2,i)]+=1
        if y2 == y1:
            for i in range(min(x1,x2), max(x1,x2)+1):
                c[(i,y2)]+=1
    count = 0
    for v in c.values():
        if v >= 2:
            count+=1
    return count

def part2(a):
    c = Counter()
    #seaFloor = [[0 for i in range(10)] for i in range(10)]
    for line in a:
        coords = line.split('->')
        initPos = coords[0].strip(' ').split(',')
        x1 = int(initPos[0])
        y1 = int(initPos[1])
        destPos = coords[1].strip(' ').split(',')
        x2 = int(destPos[0])
        y2 = int(destPos[1])
        if x2 == x1:
            for i in range(min(y1,y2), max(y1, y2)+1):
                c[(i,x2)]+=1
                #seaFloor[i][x2]+=1
        if y2 == y1:
            for i in range(min(x1,x2), max(x1,x2)+1):
                c[(y2,i)]+=1
                #seaFloor[y2][i]+=1
        dX = abs(x1-x2)
        dY = abs(y1-y2)
        if dX == dY:
            diffX = -1 if x1 > x2 else 1
            diffY = -1 if y1 > y2 else 1
            for i in range(dX+1):
                c[(y1+i*diffY,x1+i*diffX)] += 1
                #seaFloor[y1+i*diffY][x1+i*diffX]+=1
    #for line in seaFloor:
        #print(str(line).strip(']').strip('[').replace(', ', '').replace('0','.'))
    count = 0
    

    for v in c.values():
        if v >= 2:
            count+=1
    return count

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))