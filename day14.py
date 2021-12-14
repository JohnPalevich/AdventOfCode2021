from collections import Counter, defaultdict

test = "testInput/"
real = "input/"
day = "day14.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    d = defaultdict(None)
    init = a[0]
    for rule in a[2:]:
        ruleparts = rule.split(' -> ')
        d[ruleparts[0]] = ruleparts[1]
    
    for i in range(10):
        initcopy = ''.join([v for v in init])
        added = 1
        for j in range(len(init)-1):
            if d[init[j:j+2]] != None:
                initcopy = initcopy[:j+added] + d[init[j:j+2]] + initcopy[j+added:]
                added+=1
        init = initcopy
    c = Counter(init)
    most_common = c.most_common(len(c))
    return most_common[0][1] - most_common[-1][1]

def part2(a):
    d = defaultdict(None)
    for rule in a[2:]:
        ruleparts = rule.split(' -> ')
        d[ruleparts[0]] = ruleparts[1]
        
    init = Counter()
    for j in range(len(a[0])-1):
        init[a[0][j:j+2]] += 1

    for i in range(40):
        nC = Counter()
        keys = init.keys()
        for key in keys:
            if d[key] != None:
                newParts = [key[0] + d[key], d[key]+ key[1]]
                for part in newParts:
                    nC[part] += init[key]
        init = nC
    final = Counter()
    for v in init.keys():
        final[v[0]] += init[v]
    most_common = test.most_common(len(test))
    return most_common[0][1] - most_common[-1][1]+1


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))