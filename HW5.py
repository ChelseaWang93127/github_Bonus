#p1b
import random

def show_board(board):
    print("     a   b   c   d   e   f   g   h   i")
    for i in range(9):
        print("   " + "+---"*9 + "+")
        print(" %d " %(i+1), end="")
        for j in range(9):
            print("| " + board[str(i) + str(j)] + " ", end="")
        print("|")
    print("   " + "+---"*9 + "+")

#p1m
import random

#=================function and the initial 需要假設的變數(will be written in the main()later)=================
# #construct a board matrix in dictionary way
# board = {} #initialize
# for i in range(9):
# 	for j in range(9):
# 		pos = str(i) + str(j)
# 		board[pos] = ' '
# pos = input("Enter the cell (10 mines left): ")
# dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
# Gameover = False
#===============================================================================================================


#======================================show the initial board======================================
def show_board(board):
	print('     a   b   c   d   e   f   g   h   i' )
	for i in range(9):
		print('   '+'+---'*9 + '+')
		print(' %d '%(i+1), end="")
		for j in range(9):
			print('| '+ board[str(i) + str(j)] + ' ', end = "")
		print('|')
	print('   ' + '+---'*9 + '+')

#======================================the first input from the user======================================
def first_input(pos, dir):
	#因為事先選row再選col，position的位置會交錯
	pos2 = int(ord(pos[0])-96)
	pos1 = int(pos[1])
	#pos that was choosen will be recored in the mine_free
	mine_free = [str(pos1)+str(pos2)]
	for x, y in dir:
		coor_x = pos1 + x
		coor_y = pos2 + y
		if 0<=coor_x<=9 and 0<=coor_y<=9:
			mine_free.append(str(coor_x) + str(coor_y))
	return mine_free

#======================================generate mines but can't step on the minefree region======================================
def generate_mines(mine_free, dir):
	mines = []
	#chose the mine posiiton randomly
	while len(mines) <10: #why is 10? -->因為已經生成9個之後還是可以跑最後一次迴圈生成No.10
		mine = str(random.randint(1, 9)) + str(random.randint(1, 9))
		# avoid repeat and mine_free
		if mine not in mines and mine not in mine_free:
			mines.append(mine)

	#initialize the board with number in dictionary way
	board_ans = {}
	for i in range(9):
		for j in range(9):
			board_ans[str(i)+str(j)] = '0'

	# record the mines
	#notice: mines存在選取地雷時的編號是按照表格上的形式去選，所以要與程式相對應就得-1
	for m in mines:
		pos1 = int(m[0])
		pos2 = int(m[1])
		board_ans[str(pos1-1)+str(pos2-1)] = 'X'

	#count the sum fo the mines and record in that block in number form
	for i in range(9):
		for j in range(9):
			mine_sum = 0
			if board_ans[str(i)+str(j)] == 'X':
				continue
			for x, y in dir:
				coor_x = i + x
				coor_y = j + y
				if 0<=coor_x<9 and 0<=coor_y<9:
					if board_ans[str(i)+str(j)] == 'X':
						mine_sum +=1
			board_ans[str(i)+str(j)] = str(mine_sum)
	return mines, board_ans



#======================================插旗子======================================
def flag(pos, flag):
	pos2 = int(ord(pos[0])-97)
	pos1 = int(pos[1])-1
	pos3_f = pos[2]
	if board[str(pos1)+str(pos2)] == ' ':
		board[str(pos1)+str(pos2)] = 'F'
	elif board[str(pos1)+str(pos2)] == 'F':
		board[str(pos1)+str(pos2)] = ' '
	else:
		show_board(board)
		print("Can't put flag here.")
		return board
	show_board(board)
	return board


#======================================diplay the current status of the board======================================
def diaplay_status(board, board_ans, dir, pos, Gameover):
	pos2 = int(ord(pos[0])-97)
	pos1 = int(pos[1])-1

	#when the position out of the board
	if pos1>9 or pos2>9:
		show_board(board)
		print("\nInvalid cell. Enter the column followed by the row \
(ex: a5). to add or remove a flag, add 'f' to the cell (ex: a5f) \n")
		return

	#選擇上的錯誤
	#case1 there is a falg here
	if board[str(pos1)+str(pos2)] == 'F':
		show_board(board)
		print("\nThere is a flag there")
	#case2 step on the mine
	elif board_ans[str(pos1)+str(pos2)] == "X":
		print('\nGame Over!')
		show_board(board_ans)
		Gameover = True
	#case3 
	elif board[str(pos1)+str(pos2)] == ' ':
		coor = [[pos1, pos2]] #store the position that are not deal with yet
		while len(coor):
			#這一步驟確保之後新存入的coor帶處理[]的位置是固定的，只有改變數值
			pos1 = coor[0][0]
			pos2 = coor[0][1]
			#接下來這一串只是判斷那些block = ' '的位置，並且把他們儲存至代處理coor中(我卡最久的地方)
			#-------------------------------------------------------------------------------------
			if board_ans[str(pos1)+str(pos2)] == '0':
				for x, y in dir:
					coor_x = pos1 + x
					coor_y = pos2 + y
					if 0<=coor_x<9 and 0<=coor_y<9:
						if board[str(coor_x)+str(coor_y)] == ' ':
							coor.append([coor_x, coor_y])
			# -------------------------------------------------------------------------------------
			#notion: 因為最後show_board用的是board的dictionary，所以如果確定沒有東西就可以用board_ans function去計算該位置的數字，並且記錄在board dictionary內
			board[str(pos1)+str(pos2)] = board_ans[str(pos1)+ str(pos2)]
			del coor[0]
		show_board(board)
	else:
		show_board(board)
		print('The cell is already shown.')
	return board, Gameover
# ============================================main funtion(條件都寫在這)================================================================
def main():

	#status:
	Gameover = False

	#construct a board matrix in dictionary way
	board = {} #initialize
	for i in range(9):
		for j in range(9):
			pos = str(i) + str(j)
			board[pos] = ' '
	show_board(board)
	
	#print
	print("\nEnter the column followed by the row (ex: a5). To add or remove a flag, \
add 'f' to the cell (ex: a5f). Type 'help' to show this message again. \n")
	
	#input
	pos = input("Enter the cell (10 mines left): ")

	#run the 8 diraction
	dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

	#name and call the funtion
	mine_free = first_input(pos, dir)
	mines, board_ans = generate_mines(mine_free, dir)
	board, Gameover = diaplay_status(board, board_ans, dir, pos, Gameover)

	#flag on mines counting
	sum_flag = 0
	while True:
		mine = 10 - sum_flag
		#更新input顯使的mines數量
		pos = input("Enter the cell (%d mines left): "%(mine))
		if len(pos) == 2:
			board, Gameover = diaplay_status(board, board_ans, dir, pos, Gameover)
		if len(pos) == 3: #輸入有falg的時候長度為3
			board = flag(pos, flag)
		if pos == "help":
			show_board(board)
			print("\nEnter the column followed by the row (ex: a5). To add or remove a flag,\
    add 'f' to the cell (ex: a5f).")
		#接下來要去計算我差的旗子跟實際上插在'X'上的數量是否一樣，並且也要看我到底有沒有插對
		sum_flag = 0
		flag_on_mine = 0
		for i in range(9):
			for j in range(9):
				if board[str(i)+str(j)] == 'F':
					sum_flag+=1
					#寫在裡面是因為我只需要判斷我插旗子的地方是不是地雷就好
					if board[str(i)+str(j)] == 'X':
						flag_on_mine +=1
		if sum_flag == flag_on_mine == 10:
			Gameover = True
			print('\nYou win the game!')
		if Gameover:
			break

main()

#p2
#Two Player Dice Rice

#p3
# Movie Data Analysis
file_name = "IMDB-Movie-Data.csv"
f = open(file_name, 'r')
line = f.read()
line_list = line.split('\n')
clean_data = []
for line in line_list:
	clean_data.append(line.split(','))
del clean_data[0] #delete the columns title
del clean_data[-1] #末尾的空行
f.close()

# Q1 Top3 movies in 2016:
def Quesiton_1():
	data=  []
	for d in clean_data:
		if d[5] == '2016':
			data.append(d)

	#comparing the rating
	for i in range(len(data)):
		for j in range(0, len(data)-i -1):
			if data[j][7] < data[j+1][7]:
				data[j], data[j+1] = data[j+1], data[j]
	top1, top2, top3 = data[0][1], data[1][1], data[2][1]
	rank_m = [top1, top2, top3]
	for n in range(1, 4):
		print('Q1:The top%s movie is %s'%(n, rank_m[n-1]))

#Q2 derector who involves in the most movies
def Quesiton_2():
	directors = {}
	data = clean_data
	directors_lst = [d[3] for d in data]
	for d in directors_lst:
		if d not in directors:
			directors[d] = 1
		else:
			directors[d] += 1
	#comparing
	sorted_dir = dict(sorted(directors.items(), key= lambda x:x[1], reverse = True))
	top1 = list(sorted_dir.keys())[0]
	print('\nQ2:Director %s involves in the most movies.'%(top1))

#Q3 the actor generaitng highest total revenue
def Question_3():
	data = clean_data
	for i in range(len(data)):
		data[i][4] = data[i][4].split('|')
		#去除空格
		for j in range(len(data[i][4])):
			data[i][4][j] = data[i][4][j].split()
	actors = {}
		


#==================================operation:======================================
print()
Quesiton_1()
Quesiton_2()

#p4
def evaluation(eq, character):
    try:



