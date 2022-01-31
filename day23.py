from collections import deque,defaultdict
test = "testInput/"
real = "input/"
day = "day23.txt"



def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a


def part1(a):
    memo = defaultdict(lambda: -5)
    energyUsage = {'A':1, 'B':10,'C':100, 'D':1000}
    finalRoom = {'A':2, 'B':4, 'C':6, 'D':8}
    nextMoves = {0:[1], 1:[0,2], 2:[1,3,11], 3:[2,4], 4:[3,5,12], 5:[4,6], 6:[5,7,13], 7:[6,8], 8:[7,9,14], 9:[8,10], 10:[9], 11:[2,15], 12:[4,16], 13:[6,17], 14:[8,18],15:[11],16:[12],17:[13],18:[14]}

    def moveChar(burrow,energyUsed):
        if memo[burrow] != -5 and energyUsed > memo[burrow]:
            return memo[burrow]
        possibleMoves = set()
        #Check Hallways for any that can move into final state

        #Check Top Level Burrows for any that can move into final state

        #Check Bottom Level Burrows for any that can move into final state (assuming top level empty)

        #Check Top level burrows for any that are covering ones not in final state

        #Check bottom level burrows for any that are not in final state but can move from position.
        
    burrow = tuple(('' for v in range(len(a[1][1:-1]))))
    rooms = tuple((tuple((v for v in l[1:-1])) for l in a[2:4]))
    burrow = (burrow, rooms[0],rooms[1])
    for l in burrow:
        print(l, len(l))
    moveChar(burrow, 0)
    return memo[(('', '', '', '', '', '', '', '', '', '', ''), ('#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#'), (' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', ' '))]

def part2(a):
    return


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
#print(part1(input))
#print(part2(testInput))
#print(part2(input))