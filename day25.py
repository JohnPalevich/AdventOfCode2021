test = "testInput/"
real = "input/"
day = "day25.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def moveEast(board):
    newBoard = [['.' for v in l] for l in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == len(board[0])-1:
                if board[i][j] == '>':
                    if board[i][0] == '.':
                        newBoard[i][0] = '>'
                    else:
                        newBoard[i][j] = '>'
            else:
                if board[i][j]=='>': 
                    if board[i][j+1] == '.':
                        newBoard[i][j+1] = '>'
                    else:
                        newBoard[i][j] = '>'
    return newBoard

def moveDown(board, newBoard):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+1 == len(board):
                if board[i][j] == 'v':
                    if board[0][j] != 'v' and newBoard[0][j] == '.':
                        newBoard[0][j] = 'v'
                    else:
                        newBoard[i][j] = 'v'
            else:
                if board[i][j]=='v': 
                    if board[i+1][j] != 'v' and newBoard[i+1][j] == '.':
                        newBoard[i+1][j] = 'v'
                    else:
                        newBoard[i][j] = 'v'
    return newBoard

def part1(a):
    seacucumberBoard = [[v for v in l] for l in a]
    nboard = moveEast(seacucumberBoard)
    nboard = moveDown(seacucumberBoard, nboard)
    steps = 1
    while nboard != seacucumberBoard:
        seacucumberBoard = nboard
        nboard = moveEast(seacucumberBoard)
        nboard = moveDown(seacucumberBoard, nboard)
        steps+=1
    return steps

def part2(a):
    return


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
#print(part2(testInput))
#print(part2(input))