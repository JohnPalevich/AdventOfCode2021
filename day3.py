

test = "testInput/"
real = "input/"
day = "day3.txt"
def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    gamma = epsilon = ''
    tot = []
    for i in range(len(a[0])):
        tot.append(sum([int(l[i]) for l in a]))
    for v in tot:
        gamma +='1' if int(v)>len(a)/2 else '0'
        epsilon += '0' if int(v) > len(a)/2 else '1'
    return int(gamma,2) * int(epsilon,2)
 
def part2(a):
    predOxy = predCO2 = ''
    possOxyVals = possCO2Vals = a
    for i in range(len(a[0])):
        totOxy = sum([int(l[i]) for l in possOxyVals])
        totCO2 = sum([int(l[i]) for l in possCO2Vals])
        predOxy += '1' if totOxy >= len(possOxyVals)/2 else '0'
        predCO2 += '0' if totCO2 >= len(possCO2Vals)/2 else '1'
        newPossOxyVals = [] if len(possOxyVals) > 1 else possOxyVals
        newPossCO2Vals = [] if len(possCO2Vals) > 1 else possCO2Vals
        for v in possOxyVals:
            if v.startswith(predOxy):
                newPossOxyVals.append(v)
        for v in possCO2Vals:
            if v.startswith(predCO2):
                newPossCO2Vals.append(v)
        possOxyVals = newPossOxyVals
        possCO2Vals = newPossCO2Vals
    return int(possOxyVals[0],2) * int(possCO2Vals[0],2)

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))