import binascii

test = "testInput/"
real = "input/"
day = "day16.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

class Node:
    def __init__(self, id, isOperation, value):
        self.id = id
        self.isOperation = isOperation
        self.children = []
        self.value = value
    
    def getID(self):
        return self.id
    
    def getOperation(self):
        return self.isOperation
    
    def getChildren(self):
        return self.children
    
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
    
    def addChild(self, child):
        self.children.append(child)
        
def literal_value(string):
    binary = ''
    length = 0
    while string[0] == '1':
        binary+= string[1:5]
        string = string[5:]
        length+=5
    binary+= string[1:5]
    length += 5
    num = int(binary, 2)
    #print('Literal:', num)
    return num, length 

def parse_packet(binnum):
    #print('Binnum:',binnum)
    version_sum = int(binnum[:3],2)
    #print('Version', version_sum)
    packet_type = int(binnum[3:6],2)
    #print('Version seen:', version_sum)
    #print('Binary:', binnum)
    if packet_type == 4:
        n, l = literal_value(binnum[6:])
        currNode = Node(packet_type, False, n)
        return version_sum, 6 + l, currNode 
    else:
        length_id = binnum[6]
        currNode = Node(packet_type, True, 0)
        if length_id == '0':
            bits_to_parse = int(binnum[7:7+15], 2) + 7+15
            #print('Bits to parse:', bits_to_parse-7-15)
            bits_parsed = 7+15
            while bits_parsed < bits_to_parse:
                #print('Packet parsing:', binnum[bits_parsed:bits_to_parse])
                vsum, bts_parsed, child = parse_packet(binnum[bits_parsed: bits_to_parse])
                version_sum += vsum
                bits_parsed += bts_parsed
                currNode.addChild(child)
                #print('Finished')
        elif length_id == '1':
            packets_parsed = 1
            packets_to_parse = int(binnum[7:7+11],2)
            #print('Packets to parse:', packets_to_parse)
            bits_parsed = 7+11
            while packets_parsed <= packets_to_parse:
                #print('Parsing', packets_parsed, 'of', packets_to_parse)
                vsum, bts_parsed, child= parse_packet(binnum[bits_parsed:])
                version_sum += vsum
                bits_parsed += bts_parsed
                packets_parsed += 1
                currNode.addChild(child)
                #print('Finished')
        return version_sum, bits_parsed, currNode
    #print(binnum, version, packet_type)

def evaluate(node):
    if not node.getOperation():
        return node.getValue()
    if node.getID() == 0:
        v = 0
        for child in node.getChildren():
            v += evaluate(child)
        return v
    if node.getID() == 1:
        v = 1
        for child in node.getChildren():
            v *= evaluate(child)
        return v
    if node.getID() == 2:
        v = 100000000000
        for child in node.getChildren():
            val = evaluate(child)
            if val < v:
                v = val
        return v
    if node.getID() == 3:
        v = -1
        for child in node.getChildren():
            val = evaluate(child)
            if val > v:
                v = val
        return v
    if node.getID() == 5:
        children = node.getChildren()
        return 1 if evaluate(children[0]) > evaluate(children[1]) else 0
    if node.getID() == 6:
        children = node.getChildren()
        return 1 if evaluate(children[0]) < evaluate(children[1]) else 0
    if node.getID() == 7:
        children = node.getChildren()
        return 1 if evaluate(children[0]) == evaluate(children[1]) else 0

def part1(a):
    binnum =  bin(int(a[0], 16))[2:].zfill(len(a[0]*4))
    vsum, _, _ = parse_packet(binnum)
    return vsum

def part2(a):
    binnum =  bin(int(a[0], 16))[2:].zfill(len(a[0]*4))
    _, _, root = parse_packet(binnum)
    value = evaluate(root)
    return value

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))