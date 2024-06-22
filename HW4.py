#p1
# ============================Minesweeper=============================
import random

#----------------------create a board including mines------------------
def Initialise_board(row, col, num_mines):
	#create a board with mines
	board = [[" " for _ in range(cols)]for _ in range(rows)]
	#使用random funciton隨意放置地雷
	for _ in range(num_mines):
		row = random.randint(0, rows-1)
		col = random.randint(0, cols-1)
		#由於random function會有重複的疑慮，所以還是要check
		while board[row][col] == "X": #如果重複就重新再random一次
			row = random.randint(0, rows-1)
			col = random.randint(0, cols-1)
		board[row][col] = "X"
	return board

#---------------------------print a board---------------------------
def Print_Board(board):
	print("     a   b   c   d   e   f   g   h   i")
	for i in range(len(board)):
		print("   " + "+---" * 9 + "+") #最前面數字加空格長度為3
		print(" %s "%(i+1), end="")
		for j in range(9):
			print("| " + board[i][j] +" ", end="")
			if j == 8: #最後一個
				print("|")
	print("   " + "+---" * 9 + "+")

#-------------------------handle player's input------------------------
#pos:player's input
def Handle_input(board, pos):
	if pos[-1] == "f":
		pos = pos[:-1]
		print("You added a flag at position", pos)
	else:
		row = int(pos[1]) -1
		col = int(ord(pos[0]-97))
		if board[row][col] == "X":
			print("Game over! You stepped on a mine.")
		else:
			#要reveal數字
			Reveal_adjacent(board, row, col)

# ----------------------------檢視相鄰空格並顯示數字------------------------
def Reveal_adjacent(board, row, col):
	if board[row][col] == "X":
		return #這邊就像是break的概念
	rows, cols = len(board), len(board[0])#為了使代碼具有通用性，也就是之後如果更改大小的話會比較方便
	directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
	stack = [(row, col)] #起始位置*(同時把位置寫成tuple form)

	while stack: #list不為空
		cur_row, cur_col = stack.pop()
		for dr_row, dr_col in directions:
			new_row = cur_row + dr_row
			new_col = cur_col + dr_col
			if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == ' ':
				board[new_row][new_col] = str(random.randint(1, 9))
				stack.append((new_row, new_col))

# <chat GPT method1 provided>
# def reveal_adjacent(board, row, col):
#     if board[row][col] != ' ':
#         return
# 	for i in range(-1, 2): #[-1~1]-->(走過附近八)
# 		for j in range(-1, 2):
# 			new_row = row + i
# 			new_col = row + j
# 			#確保new的index在範圍之內
# 			if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == ' ':
# 				board[new_row][new_col] = random.randint(1, 9)
# 				Reveal_adjacent(board, row, col) #函式循環

# 遊戲初始化(一開始寫在前面，但是因為要寫在def後面，最後會一到最後面)
rows, cols = 9, 9
num_mines = 10
board = Initialise_board(rows, cols, num_mines)
Print_Board(board)
print("Enter the column followed by the row (ex: a5). To add or remove a flag,\n add 'f' to the cell (ex: a5f). Type 'help' to show this message again ")

while True:
	pos = input("Enter the cell(10 miles left): ")
	if pos.lower() == "help":
		print("Enter the column followed by the row (ex: a5). To add or remove a flag,\n add 'f' to the cell (ex: a5f). Type 'help' to show this message again ")
		continue
	Handle_input(board, pos)
	Print_Board(board)

#p2
# Black jack
# 一副洗好的牌52
# 玩家先拿取兩張
# 加牌:hitting/ 停止:staying
# if玩家牌21 --> black jack
# if玩家牌>21 --> busts--> lose -->停止加牌
# 如果手上同時擁有jack ace --> black jack
# 牌面:2-10(數字)，JQK(10)，ACE(1 or 11)
# dealer牌面至少要17
# ===================================詳解版==============================================
print() #排版用
import random #本題要學會使用random function
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #牌面數值
suits = ["C", "D", "H", "S"] #牌面花色

#-----------------------定義一個洗牌的函數--------------------------
def ShuffleDeck():
	deck = [] #empty lst for storing洗過的牌
	# 單純先生出一副樸克牌
	for i in suits: #先挑花色
		for j in ranks: #在選數字
			deck.append(i+j) #合併
	# 然後才是洗牌
	random.shuffle(deck) #洗牌的意思*()這個random函數的運用
	return deck #把洗好的牌回傳

#-------------------------抽牌-----------------------------------
def drawCards(deck, num): #由於會使用到def ShuffleDeck()裡面已經定義過的自變數，有點像是在一個函數裡面呼叫另一個韓式的概念
	cards = [] #empty lst for storing抽的牌
	for i in range(num):
		card = deck.pop(0) #抽出最上面的牌
		cards.append(card)	#加到cards的list中
	return cards

#--------------------------計算當前牌面---------------------------------
def cal_card_value(hand):
	tol_value = 0
	for card in hand:
		card_value = card[1:] #因為樸克牌形式長成e.g:"C8"，我們只想提取後面的數字
		#ACE
		if card_value == "A":
			#決定A要當10還是11的條件
			if tol_value <= 10:
				tol_value += 11
			else:
				tol_value += 1
		#JQK
		elif card_value in ["J", "Q", "K"]:
			tol_value += 10
		#NUM
		else:
			tol_value += int(card_value)
	return tol_value

# -----------------------hit or stay--------------------------------
#呼叫函數
deck = ShuffleDeck() #洗好的牌
player = drawCards(deck, 2) #player先抽兩張
dealer = drawCards(deck, 2)
tol_value_p = cal_card_value(player) #計算總數值
tol_value_d = cal_card_value(dealer)


#**********************計算player加牌後的value****************************
#先告訴你你目前的狀況
print("Your current value is",tol_value_p)
print("With the hand",player)

while tol_value_p < 21:
	hs_ornot = int(input("\nHit or Stay? (Hit = 1, Stay = 0): "))
	print()
	#if hitting
	if hs_ornot == 1:
		card = deck.pop(0) #一樣從現有的牌抽出最後一張
		print("You draw",card) #告訴你抽到甚麼牌
		print()
		player.append(card) #因為drawCards fuol_value_p = cal_card_value(player)nction建立的是一個list
		tol_value_p = cal_card_value(player) #返回更新後的總點數
		if tol_value_p <= 21: #為什麼前面已經說<21才進入這個迴圈，但這邊又要提一次
			print("Your current value is",tol_value_p)
			print("With the hand",player)
	else:
		print("")
		break
#如果我跳出上面這個while迴圈
if tol_value_p== 21:
	print("Your current value is",tol_value_p)
	print("With the hand",player)
	print("\nBlack jack")
elif tol_value_p >21:
	print("Bust!(>21)")

print("---------------------------------------------\n")

#**********************計算Dealer加牌後的value*************************
print("Dealer's current value is",tol_value_d)
print("With the hand",dealer)
while tol_value_d < 21 :
	while tol_value_d <= 17:
		card = deck.pop(0)
		print("\nDealer draw",card)
		dealer.append(card)
		tol_value_d = cal_card_value(dealer)	#返回更新後的總點數
		print("\nDealer's current value is",tol_value_d)
		print("With the hand",dealer)
	if tol_value_d > 17: #題目限制
		break
if tol_value_d== 21:
	print("\nDealer's current value is",tol_value_d)
	print("With the hand",dealer)
	print("\nBlack jack")
elif tol_value_d >21:
	print("\nBust!(>21)")

#--------------------------判斷贏家---------------------------------
print()
if tol_value_p <= 21 and tol_value_d <= 21:
	# player win
	if tol_value_p > tol_value_d:
		print("~~~You beat the dealer!~~~")
	# dealer win
	elif tol_value_p < tol_value_d:
		print("~~~Dealer wins~~~")
	# draw
	elif tol_value_p == tol_value_d:
		print("~~~You tied the dealer, nobody wins~~~")
#another draw
elif tol_value_p > 21 and tol_value_d > 21:
	print("~~~You tied the dealer, nobody wins~~~")
elif tol_value_p <= 21 and tol_value_d > 21:
	print("~~~You beat the dealer!~~~")
elif tol_value_p > 21 and tol_value_d <= 21:
	print("~~~Dealer wins~~~")



