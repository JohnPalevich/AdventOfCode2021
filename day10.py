from os import close


test = "testInput/"
real = "input/"
day = "day10.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    d = {')':3, ']':57, '}' : 1197, '>':25137}
    openers = ['(','{','[','<']
    s = 0

    def ext(c, closingSequence):
        opp = {'(':')', '[':']', '{':'}', '<':'>'}
        return opp[c]+closingSequence

    def verify(c, closingSequence):
        closers = ['>','}',')',']']
        if c in closers and c != closingSequence[0]:
            return d[c], closingSequence
        else:
            return 0, closingSequence[1:]

    for l in a:
        closingSequence = ''
        for c in l:
            if c in openers:
                closingSequence = ext(c, closingSequence)
            else:
                tot, closingSequence = verify(c, closingSequence)
                if tot != 0:
                    s+=tot
                    break         
    return s



def part2(a):
    openers = ['(','{','[','<']

    def ext(c, closingSequence):
        opp = {'(':')', '[':']', '{':'}', '<':'>'}
        return opp[c]+closingSequence

    def verify(c, closingSequence):
        closers = ['>','}',')',']']
        if c in closers and c != closingSequence[0]:
            return 1, closingSequence
        else:
            return 0, closingSequence[1:]

    def calcScore(sequence):
        d = {')':1, ']':2, '}' : 3, '>':4}
        score = 0
        for c in sequence:
            score = score*5 + d[c]
        return score
    
    scores = []
    for l in a:
        closingSequence = ''
        for c in l:
            if c in openers:
                closingSequence = ext(c, closingSequence)
            else:
                tot, closingSequence = verify(c, closingSequence)
                if tot != 0:
                    closingSequence = ''
                    break
        if len(closingSequence) != 0:
            scores.append(calcScore(closingSequence))
    scores = sorted(scores)
    return scores[len(scores)//2]

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))