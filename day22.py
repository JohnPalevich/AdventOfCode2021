from collections import Counter

test = "testInput/"
real = "input/"
day = "day22.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    cubes = set()
    for line in a:
        info = line.split(',')
        frontinfo = info[0].split()
        on = frontinfo[0] == 'on'
        xinfo = frontinfo[1][2:].split('..')
        lX = int(xinfo[0])
        rX = int(xinfo[1])
        yinfo = info[1][2:].split('..')
        lY = int(yinfo[0])
        rY = int(yinfo[1])
        zinfo = info[2][2:].split('..')
        lZ = int(zinfo[0])
        rZ = int(zinfo[1])
        for x in range(max(-50, lX), min(rX, 50)+1):
            for y in range(max(-50, lY), min(rY, 50)+1):
                for z in range(max(-50,lZ), min(rZ, 50)+1):
                    if on:
                        cubes.add((x,y,z))
                    elif (x,y,z) in cubes:
                        cubes.remove((x,y,z))
    return len(cubes)

def part2(a):
    cubes = Counter()
    for i in range(len(a)):
        info = a[i].split(',')
        frontinfo = info[0].split()
        on = frontinfo[0] == 'on'
        xinfo = frontinfo[1][2:].split('..')
        lX = int(xinfo[0])
        rX = int(xinfo[1])
        yinfo = info[1][2:].split('..')
        lY = int(yinfo[0])
        rY = int(yinfo[1])
        zinfo = info[2][2:].split('..')
        lZ = int(zinfo[0])
        rZ = int(zinfo[1])
        newCubes = Counter()
        for cube in cubes.keys():
            leftX = max(lX,cube[0])
            rightX = min(rX, cube[1])
            leftY = max(lY,cube[2])
            rightY = min(rY, cube[3])
            leftZ = max(lZ,cube[4])
            rightZ = min(rZ, cube[5])
            if leftX <= rightX and leftY<=rightY and leftZ <= rightZ:
                newCubes[leftX,rightX,leftY,rightY,leftZ,rightZ] -= cubes[cube]
        if on:
            newCubes[(lX,rX,lY,rY,lZ,rZ)] += 1
        cubes.update(newCubes)
    count = 0
    for cube,sign in cubes.items():
        count+= (cube[1]-cube[0]+1)*(cube[3]-cube[2]+1)*(cube[5]-cube[4]+1)*sign
    return count

testInput = getInput(test+day)
input = getInput(real+day)
#print(part1(testInput))
#print(part1(input))
print(part2(testInput))
print(part2(input))