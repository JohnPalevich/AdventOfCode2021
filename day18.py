from os import close, lseek, register_at_fork


test = "testInput/"
real = "input/"
day = "day18.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

class Node:
    def __init__(self, left, right, depth, value, isNum):
        self.left = left
        self.right = right
        self.depth = depth
        self.value = value
        self.isNum = isNum
        self.parent = None
        
    
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right

    def setParent(self, parent):
        self.parent = parent
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getParent(self):
        return self.parent

    def setDepth(self, depth):
        self.depth = depth
    
    def getDepth(self):
        return self.depth
    
    def getIsNum(self):
        return self.isNum
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

def printTree(node):
    if node.getIsNum():
        print(node.getValue(), end = '')
    else:
        print('[', end='')
        lval = printTree(node.getLeft())
        lval.setParent(node)
        print(',', end='')
        rval = printTree(node.getRight())
        rval.setParent(node)
        print(']', end='')
    return node


def explodeNode(n):
    if n.getIsNum():
        return
    #print('Explode Value:', n.getValue())
    leftNum = n.getLeft().getValue()
    rightNum = n.getRight().getValue()
    parent = n.getParent()
    setL = False
    setR = False
    isLeft = parent.getLeft() == n
    isRight = parent.getRight() == n
    prev = n
    while parent != None:
        isLeft = parent.getLeft() == prev
        isRight = parent.getRight() == prev
        if not setL and not isLeft:
            if parent.getLeft().getIsNum():
                newLeft = Node(None, None, parent.getDepth()+1, parent.getLeft().getValue()+leftNum, True)
                newLeft.setParent(parent)
                parent.setLeft(newLeft)
                #print('1')
                setL = True
            else:
                #print('Depth', parent.getDepth())
                currNode = parent.getLeft()
                while currNode != None and not currNode.getIsNum():
                    currNode = currNode.getRight()
                currNode.setValue(currNode.getValue()+leftNum)
                #print('2')
                setL = True
            
        if not setR and not isRight:
            if parent.getRight().getIsNum():
                newRight = Node(None, None, parent.getDepth()+1, parent.getRight().getValue()+rightNum, True)
                newRight.setParent(parent)
                parent.setRight(newRight)
                #print('3')
                setR = True
            else:
                currNode = parent.getRight()
                while currNode != None and not currNode.getIsNum():
                    currNode = currNode.getLeft()
                currNode.setValue(currNode.getValue()+rightNum)
                #print('4')
                setR = True
        prev = parent
        parent = parent.getParent()
    parent = n.getParent()
    isLeft = parent.getLeft() == n
    isRight = parent.getRight() == n
    parent = n.getParent()
    replacementNode = Node(None, None, parent.getDepth()+1, 0, True)
    replacementNode.setParent(parent)
    if parent.getLeft() == n:
        parent.setLeft(replacementNode)
    else:
        parent.setRight(replacementNode)

def splitNode(n):
    lval = n.getValue()//2
    rval = -(n.getValue() // -2)
    lNode = Node(None, None, n.getDepth()+1, lval, True)
    rNode = Node(None, None, n.getDepth()+1, rval, True)
    newNode = Node(lNode, rNode, n.getDepth(), 0, False)
    parent = n.getParent()
    newNode.setParent(parent)
    if parent.getRight() == n:
        parent.setRight(newNode)
    else:
        parent.setLeft(newNode)
    return 

def traverseTreeExplode(n, root):
    if n == None:
        return False
    if not n.getIsNum() and n.getDepth() == 4:
        print('Tree Exploding: ', end='')
        printTree(root)
        print()
        explodeNode(n)
        # print('Tree Exploded: ', end='')
        # printTree(root)
        # print()
        return True
    else:
        l = traverseTreeExplode(n.getLeft(), root)
        r = traverseTreeExplode(n.getRight(), root)
        return l or r

def traverseTreeSplit(n, root):
    if n == None:
        return False
    elif n.getValue() > 9:
        #print(n.getParent(), n.getValue())
        print('Tree Splitting: ', end='')
        printTree(root)
        print()
        n = splitNode(n)
        # print('Tree Split: ', end='')
        # printTree(root)
        # print()
        return True
    else:
        return traverseTreeSplit(n.getLeft(),root) or traverseTreeSplit(n.getRight(),root)

def establishTree(info, depth):
    leftNode = None
    rightNode = None
    lStart = 0
    if info[0] != '[':
        splitVal = info[:-1].split(',')
        leftNode = Node(None, None, depth, int(splitVal[0]), True)
        lStart = info.index(',')
        #print('LeftNode:', leftNode.getValue())
    else:
        openBrackets = 0
        closeBrackets = 0
        while (openBrackets != closeBrackets or openBrackets==0) and lStart < len(info):
            if info[lStart] == '[':
                openBrackets +=1
            if info[lStart] == ']':
                closeBrackets += 1
            lStart+=1
        leftNodeInfo = info[1:lStart-1]
        #print('LeftNode:',leftNodeInfo)
        leftNode = establishTree(leftNodeInfo, depth+1)
    if info[lStart+1] != '[':
        splitVal = info[lStart+1].strip(']').split(',')
        rightNode = Node(None, None, depth, int(splitVal[0]), True)
        #print('RightNode:', rightNode.getValue())
    else:
        rStart = lStart + 1
        openBrackets = closeBrackets = 0
        while openBrackets != closeBrackets or openBrackets==0:
            if info[rStart] == '[':
                openBrackets += 1
            if info[rStart] == ']':
                closeBrackets += 1
            rStart += 1
        rightNodeInfo = info[lStart+2:rStart-1]
        #print('RightNode:', rightNodeInfo)
        rightNode = establishTree(rightNodeInfo, depth+1)
    
    n = Node(leftNode, rightNode, depth, 0, False)
    leftNode.setParent(n)
    rightNode.setParent(n)
    return n

def reduceTree(root):
    split = True
    exploded = True
    while split or exploded:
        exploded = traverseTreeExplode(root, root)
        split = traverseTreeSplit(root, root)
    return root

def updateDepths(root):
    if root == None:
        return
    else:
        root.setDepth(root.getDepth()+1)
        updateDepths(root.getRight())
        updateDepths(root.getLeft())

def part1(a):
    root = establishTree(a[0][1:-1], 0)
    print('Tree Printing: ', end='')
    printTree(root)
    print()
    reduceTree(root)
    for line in a[1:]:
        print('Tree Printing: ', end='')
        printTree(root)
        print()
        root1 = root
        updateDepths(root1)
        root2 = establishTree(line[1:-1], 1)
        root = Node(root1, root2, 0, 0, False)
        root1.setParent(root)
        root2.setParent(root)
        reduceTree(root)
    
    print('Tree Printing: ', end='')
    printTree(root)
    print()
    return

def part2(a):
    return


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
#print(part1(input))
#print(part2(testInput))
#print(part2(input))