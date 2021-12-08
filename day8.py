from collections import deque

test = "testInput/"
real = "input/"
day = "day8.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    c = 0
    for line in a:
        part = line.split('|')
        fourDig = part[1].split()
        for dig in fourDig:
            lens = [2,3,4,7]
            if len(dig) in lens:
                c+=1
    return c

def part2(a):
    c = 0
    for line in a:
        part = line.split('|')
        info = part[0].split()
        digits = {}
        key = {}
        queue = deque(info)
        while(len(digits.keys())!= 4):
            val = queue.popleft()
            if len(val) == 7:
                digits[val] = 8
                key['e'] = {v for v in val}
                key['g'] = {v for v in val}
            elif len(val) == 2:
                digits[val] = 1
                key['c'] = {v for v in val}
                key['f'] = {v for v in val} 
            elif len(val) == 3:
                digits[val] = 7
                key['a'] = {v for v in val} 
            elif len(val) == 4:
                digits[val] = 4
                key['b'] = {v for v in val}
                key['d'] = {v for v in val} 
            else:
                queue.append(val)

        key['e'] = key['g'] = key['g'].difference(key['a']).difference(key['b'])
        key['a'] = key['a'].difference(key['c'])
        key['b'] = key['b'].difference(key['c']) 
        key['d'] = key['d'].difference(key['c'])

        tot = {'a','b','c','d','e','f','g'}
        while(len(queue)!=3):
            val = queue.popleft()
            #case that it is 0, 6, or 9 
            if len(val) == 6:
                remVal = tot.difference({v for v in val})
                possWires = tot.difference({wire for wire in ['e', 'c', 'd'] if len(key[wire]) == 2})
                for wire in possWires:
                    key[wire] = key[wire].difference(remVal)
            else:
                queue.append(val)

        remWires = [possWire for possWire in key.keys() if len(key[possWire]) == 2]
        seenWires = [key[possWire] for possWire in key.keys()if len(key[possWire]) == 1]
        for wire in seenWires:
            for remWire in remWires:
                key[remWire] = key[remWire].difference(wire)

        fourDig = part[1].split()
        num = 0
        match = {frozenset({'a','b','c','e','f','g'}):0,
                frozenset({'c','f'}):1,
                frozenset({'a','c','d','e','g'}):2,
                frozenset({'a','c','d','f','g'}):3,
                frozenset({'b','c','d','f'}):4,
                frozenset({'a','b','d','f','g'}):5,
                frozenset({'a','b','d','e','f','g'}):6,
                frozenset({'a','c','f'}):7,
                frozenset({'a','b','c','d','e','f','g'}):8,
                frozenset({'a','b','c','d','f','g'}):9
                }
        newKey = {frozenset(v):k for k,v in key.items()}
        for dig in fourDig:
            s = set()
            for d in dig:
                s.update(newKey[frozenset(d)])
            num = 10*num + match[frozenset(s)]
        c += num
    return c

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))