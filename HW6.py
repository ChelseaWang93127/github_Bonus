#p1
def candy_crush(board):
    # determine the row and column
    row = len(board)
    col = len(board[0])
    endgame = False

    while not endgame:
        endgame = True
        # 存放可消除的座標
        coor = set()
        # 檢查可消除的糖果，並將座標加入 coordinate 的 set 中
        for i in range(row):
            for j in range(col):
                candy = board[i][j]
                # zero case
                if candy == "0":
                    continue

                # veritcal 
                if j+2 < col and board[i][j+1] == board[i][j+2] == candy:
                    # 利用 union 函數取聯集
                    coor = coor.union({(i, j), (i, j+1), (i, j+2)})
                # horizontal
                if i+2 < row and board[i+1][j] == board[i+2][j] == candy:
                    coor = coor.union({(i, j), (i+1, j), (i+2, j)})
        
        # 消除後為0
        for x, y in coor:
            board[x][y] = "0"
            endgame = False
        # drop candy
        for j in range(col):
            dis = 0
            for i in range(row-1, -1, -1):
                # 計算需落下幾格
                if board[i][j] == "0":
                    dis += 1
                # 遇到非0的糖果 & 距離>0
                elif dis > 0:
                    board[i+dis][j] = board[i][j]
                    board[i][j] = "0"
                    

    return board

filename1 = "candy_input1.txt"
filename2 = "candy_input2.txt"

# load input1
with open(filename1, "r") as f:
    board1 = []
    for line in f.readlines():
        line=line.strip("\n")
        board1.append(line.split(","))
    f.close()

# load input2
with open(filename2, "r") as f:
    board2 = []
    for line in f.readlines():
        line = line.strip("\n")
        board2.append(line.split(","))
    f.close()

# update new board
result1 = candy_crush(board1)
result2 = candy_crush(board2)

# write in txt
path1 = "candy_output1.txt"
path2 = "candy_output2.txt"

with open(path1, "w") as f:
    for l in result1:
        for n in l:
            f.writelines(n)
            f.writelines(",")
        f.writelines("\n")

with open(path2, "w") as f:
    for l in result2:
        for n in l:
            f.writelines(n)
            f.writelines(",")
        f.writelines("\n")



#p2
import random


def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

# generate the board
def initialize_board(width, height, candyTypes):
    board = []
    for _ in range(height):
        row = [random.randint(1, candyTypes) for _ in range(width)]
        board.append(row)
    return board

# check if achieving elimination
def check_eliminate(board, height, width):
    coor = set()
    for i in range(height):
        for j in range(width):
            candy = board[i][j]
            if candy == 0:
                continue
            # vertical 
            if j+2 < width and board[i][j+1] == board[i][j+2] == candy:
                coor = coor.union({(i, j), (i, j+1), (i, j+2)})
            # horizontal
            if i+2 < height and board[i+1][j] == board[i+2][j] == candy:
                coor = coor.union({(i, j), (i+1, j), (i+2, j)})
    return coor

def eliminate(board, height, width, candyTypes, first=False):
    endRound = False
    score = 0

    while not endRound:
        endRound = True
        coor = check_eliminate(board, height, width)

        for i in range(len(coor)):
            score += 10
        for x, y in coor:
            board[x][y] = 0
            endRound = False
        
        # drop candy
        for j in range(width):
            dis = 0
            for i in range(height-1, -1, -1):
                if board[i][j] == 0:
                    dis += 1
                elif dis > 0:
                    board[i+dis][j] = board[i][j]
                    board[i][j] = 0
                    
        # randomly drop new candy
        for i in range(height):
            for j in range(width):
                if board[i][j] == 0:
                    board[i][j] = random.randint(1, candyTypes)
                    endRound = False

        # print every boards when dropping
        if (not endRound) and (not first):
            print("Candies dropping! Achieve crushed")
            print("Gaining points from the board:",score)
            print("Current board: ")
            print_board(board)
            print()
    return board, score

def switch_candy(board, row1, col1, row2, col2):
    # switch
    board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]

# test if switches can achieve elimination
def check_mutable(board, height, width, candyTypes):
    # check horizental switch 
    for i in range(height):
        for j in range(width-1):
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            coor = check_eliminate(board, height, width)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            if coor:
                return True
    # check vertical switch
    for i in range(height-1):
        for j in range(width):
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            coor = check_eliminate(board, height, width)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            if coor:
                return True
    
    return False

# if the board is not mutable, regenerate a new board
def regenerate_board(board, mutable, height, width, candyTypes):
    if not mutable:
        board = initialize_board(width, height, candyTypes)
        board, s = eliminate(board, height, width, candyTypes)
    return board

def main():
    height = int(input("Input the height of the height: "))
    width = int(input("Input the width of the board: "))
    candyTypes = int(input("Input the number of candy types: "))

    board = initialize_board(width, height, candyTypes)
    # set up numbers of operations
    num_op = int(height * width / 3)
    # score threshold
    threshold = num_op * 60
    scores = 0

    board, s = eliminate(board, height, width, candyTypes, first=True)
    print("The initial board: ")
    print_board(board)
    print()
    print("You have to achieve %d points in %d steps to win the game" %(threshold, num_op))
    print("Game started!!")
    
    

    while num_op:
        # check if mutable
        mutable = check_mutable(board, height, width, candyTypes)
        if not mutable:
            print("Does not exist switches that can achieve eliminating, generating a new board!")
            board = initialize_board(width, height, candyTypes)
            board, s = eliminate(board, height, width, candyTypes)

        # input two adjacent cells to switch
        while True:
            try:
                r1, c1 = map(int, input("Input 1st cell to switch (ex: 0 2): ").split())
                r2, c2 = map(int, input("Input 2nd cell to switch (ex: 0 3): ").split())
                switch_candy(board, r1, c1, r2, c2)
                coor = check_eliminate(board, height, width)
                if not len(coor):
                    raise
                print("Before elimination: ")
                print_board(board)
                print("-"*30)
            except:
                print("No elimination can be achieved, try a different one")
                # switch back
                switch_candy(board, r1, c1, r2, c2) 
            else:
                break
        # do elimination
        board, s = eliminate(board, height, width, candyTypes)
        scores += s
        print("After elimination: ")
        print_board(board)
        num_op -= 1
        print("Remaining times: ", num_op)
        print("Current score: ", scores)
        print("-"*30)

        # win case
        if scores > threshold:
            print("Congratulations! You win this game.")
            return 
    # loss case
    print("Sorry, you lose the game!")
        
main()
