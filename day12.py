from collections import defaultdict
from collections import Counter

test = "testInput/"
real = "input/"
day = "day12.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

class Node:
    def __init__(self, value, big):
        self.value = value
        self.big = big
        self.seen = False
        self.connectedTo = set()
    
    def getVal(self):
        return self.value

    def getBig(self):
        return self.big
    
    def getSeen(self):
        return self.seen

    def setSeen(self, newVal):
        self.seen = newVal
    
    def getNeighbors(self):
        return self.connectedTo

    def addNeighbor(self, neighbor):
        self.connectedTo.add(neighbor)


def part1(a):
    d = defaultdict(str)
    paths = set()

    def updateGraph(n, other):
        if d[n] == '':
            d[n] = Node(n, n.isupper())
        if d[other] == '':
            d[other] = Node(other, other.isupper())
        d[n].addNeighbor(d[other])
        d[other].addNeighbor(d[n])

    def dfs(startNode, pre):
        if startNode.getVal() == 'end':
            return pre + ',' + 'end'
        pre = pre+','+startNode.getVal()
        if not startNode.getBig():
            startNode.setSeen(True)
        for neighbor in startNode.getNeighbors():
            if not neighbor.getSeen():
                retStr = dfs(neighbor, pre)
                if 'end' in retStr:
                    paths.add(retStr)
        if not startNode.getBig():
            startNode.setSeen(False)
        
        return ''

    for l in a:
        nodes = l.split('-')
        firstNode = nodes[0]
        secondNode = nodes[1]
        updateGraph(firstNode, secondNode)
    #DFS All paths
    dfs(d['start'], '')
    return len(paths)

def part2(a):
    d = defaultdict(str)
    paths = set()
    global seenTwice
    seenTwice = False
    
    def updateGraph(n, other):
        if d[n] == '':
            d[n] = Node(n, n.isupper())
        if d[other] == '':
            d[other] = Node(other, other.isupper())
        d[n].addNeighbor(d[other])
        d[other].addNeighbor(d[n])
    
    def dfs(startNode, pre):
        global seenTwice
        if startNode.getVal() == 'end':
            return pre + ',' + 'end'
        
        pre = pre+','+startNode.getVal()
        
        if not startNode.getBig():
            startNode.setSeen(True)
        
        for neighbor in startNode.getNeighbors():
            if not neighbor.getSeen():
                retStr = dfs(neighbor, pre)
                if 'end' in retStr:
                    paths.add(retStr[1:])
            elif neighbor.getSeen() and neighbor.getVal() != 'start' and not seenTwice:
                neighbor.setSeen(False)
                seenTwice = True
                retStr = dfs(neighbor, pre)
                if 'end' in retStr:
                    paths.add(retStr[1:])
                neighbor.setSeen(True)
                seenTwice=False

        if not startNode.getBig():
            startNode.setSeen(False)
        
        return ''

    for l in a:
        nodes = l.split('-')
        firstNode = nodes[0]
        secondNode = nodes[1]
        updateGraph(firstNode, secondNode)

    dfs(d['start'], '')
    return len(paths)


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))