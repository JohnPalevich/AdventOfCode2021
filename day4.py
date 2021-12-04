test = "testInput/"
real = "input/"
day = "day4.txt"
def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def addNum(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j][0] == num:
                board[i][j] = (num, True)
                return board
    return board

def checkBingo(board):
    for i in range(5):
        bingo = True
        for j in range(5):
            if board[i][j][1] == False:
                bingo = False
        if bingo:
            return True
    for j in range(5):
        bingo = True
        for i in range(5):
            if board[i][j][1] == False:
                bingo = False
        if bingo:
            return True
    bingo = True
    for i in range(5):
        if board[i][i][1] == False:
            bingo = False
    if bingo:
        return True
    for i in range(5):
        if board[i][4-i][1] == False:
            return False

def calcScore(board, num):
    tot = 0
    for i in range(5):
        for j in range(5):
            if not board[i][j][1]:
                tot+= int(board[i][j][0])
    return tot * int(num)

def part1(a):
    numbers = a[0].split(',')
    boards = []
    remIn = a[2:]
    for i in range(0, len(remIn), 6):
        board = [[(val, False) for val in line.split() ] for line in remIn[i:i+5]]
        boards.append(board)
    for num in numbers:
        for b in range(len(boards)):
            boards[b] = addNum(boards[b], num)
            if checkBingo(boards[b]):
                return calcScore(boards[b], num)
    return 0
 
def part2(a):
    numbers = a[0].split(',')
    boards = []
    remIn = a[2:]
    d = {}
    for i in range(0, len(remIn), 6):
        board = [[(val, False) for val in line.split() ] for line in remIn[i:i+5]]
        d[int(i/6)] = (0, 0)
        boards.append(board)
    seen = 0
    for num in numbers:
        for b in range(len(boards)):
            boards[b] = addNum(boards[b], num)
            if checkBingo(boards[b]):
                if d[b] == (0,0):
                    seen += 1
                    d[b] = (seen, calcScore(boards[b], num))
    return max(d.values())[1]

print(part1(getInput(test + day)))
print(part1(getInput(real + day)))
print(part2(getInput(test + day)))
print(part2(getInput(real + day)))