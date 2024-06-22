#p1
# ----------------------------------problem-1-Fine-the-last-ID------------------------------------------
num_total_stu = int(input("Input the total number of students(n>0):"))

#想法:設立一個list，裡面放從1開始到使用者輸入的數字
#接著每數三個，就去掉那個數字，然後一直循環直到只剩下一個數字

stu = [i for i in range(1, num_total_stu+1)] #這就是一個用法，前面的i不能省，而且要初始化變數
num = 0 #代表往後'數'的數字，只要num=3就去掉那個數字，每3個一循環
i = 0 	#代表當前學生的索引(圓桌還剩下多少人)

while len(stu)!=1: 	#如果最後數量剩下1那就停止
	is_third_num = False
	num = num + 1

	if num == 3:
		stu.remove(stu[i])
		num = 0 #再重新數一次
		is_third_num = True
	if not is_third_num:
		i = i+1 #如果這個人他並不是被數到的第三個，那就會繼續往下數
	if i == len(stu): #這個代表的是，當我想要取的索引值i已經超出了現有列表的長度，那就代表要重新回到最一開始，重新去跑當數到3的時候要去除的數字
		i = 0 
# 針對21行做更進一步的解釋，這邊是為了去'檢測'ID跑到的地方有沒有已經超出了list所擁有數值的範圍
print("The last ID is:",stu[0])

#p2
# ------------------------------------------Problem2-Evaluaiton-of-Polynomial-strings-----------------------------------------
poly = input("Input polynomial:")
x = value_X = int(input("Input the value of X:"))
# 切割
poly = list(poly)
print(poly)
# 先把全部可能的狀況都寫出來: X^4+23*X^3+17*X^2+9453
# ====================需要考慮的點:======================================
# 1.切割成list之後會有十位數以上被切分開的情形，要想辦法合併
# 2.因為輸入的格式為字串，被切割之後也是以字串形式存在，需要將其轉換為數字
# 3.如果在刪除list中的index時會改變字串的大小，因此就把變數歸零



# 合併十位數以上
i = 0
while i+1 < len(poly):
	if poly[i].isdigit() and poly[i+1].isdigit() :
		poly[i] = poly[i]+poly[i+1]
		del poly[i+1]
		continue
	i += 1
# ===outcome===
# print(poly)



i = 0
while i <len(poly):
	# 將字串(數字)轉成數字
	if poly[i].isdigit():
		poly[i] = int(poly[i])
	# 將變數轉換成數字
	if poly[i] == "X":
		poly[i] = x #轉成用戶輸入的數值(變數)
	i += 1
# ===outcome===
# print(poly)
# ['X', '^', '4', '+', '2', '3', '*', 'x', '^', '3', '+', '1', '7', '*', 'X', '^', '2', '+', '9', '4', '5', '3']
# [-11, '^', 4, '+', 23, '*', 'x', '^', 3, '+', 17, '*', -11, '^', 2, '+', 9453]

#如果負號在一開頭的地方，合併到正後方的數字或是變數
if poly[0] == "-":
	poly[1] = -1*poly[1]
	del poly[0]
# ===outcome===
# print(poly)


# ------------------------處理運算符號------------------------------

# "^"
i = 0
while i < len(poly):
	if poly[i] == "^":
		poly[i] = int(poly[i-1]) ** poly[i+1]
		del poly[i-1]
		del poly[i]
		i = 0	
	i += 1
# ===outcome===
# print(poly)


#"*"
i = 0
while i < len(poly):
	if poly[i] == "*":
		poly[i] = poly[i-1] * poly[i+1]
		del poly[i-1]
		del poly[i]
		i = 0
	i += 1
# ===outcome===
# print(poly)



# "+,-"
i = 0
while i < len(poly):
	if poly[i] == "+":
		poly[i] = poly[i-1] + poly[i+1]
		del poly[i-1]
		del poly[i]
		i = 0

	if poly[i] == "-":
		poly[i] = poly[i-1] - poly[i+1]
		del poly[i-1]
		del poly[i]
		i = 0

	i+=1

print("Evaluate result:", poly[0])

# 註解:我與莊學長不同的地方，(就是為何我在delete的部分會出錯，是因為他先去除掉的是後面的數字，所以就不會影響前面index數值的去除，但是如果我先去除前面的，就會變成後面的list順序需要重新來過)

#p3
#------------------Print-game-board-----------------------
for i in range(6):
	print("+---"*7 + "+")
	print("|   "*7 + "|")
print("+---"*7 + "+")
for num in range(7):
	print("  " + str(num) + " ", end = "")

playerX = True
done = False
rang = [0, 1, 2, 3, 4, 5, 6]
col = [[" " for i in range(7)] for j in range(6)] #初始化空格

while not done:
	if playerX:
		column = input("Player X >> ")
	else:
		column = input("Player O >> ")

	#檢測是否valid
	if column.isdigit():
		column = int(column) #重新輸入的意思
		if column not in rang:
			print("Out of range, try again [0-6]")
			continue
		else:
			if col[0][column] != " ":
				print("This column is full. Try another column.")
				continue
	else:
		print("Invalid input, try again [0-6].")
		continue

	if playerX:
		for i in range (6):
			if col[5-i][column] == " ":
				col[5-i][column] = "X"
				break
	else:
		for i in range (6):
			if col[5-i][column] == " ":
				col[5-i][column] = "O"
				break
	playerX = not playerX #切換玩家

	#---------------換人之後當下的game board改變--------------
	# 程式碼之所以要等到切換玩家後才執行
	# 是因為遊戲板中的棋子位置在每次玩家下棋後可能會有所改變
	# 因此需要在切換玩家後重新打印整個遊戲板
	# 以確保玩家看到的是最新的遊戲狀態
	for i in range(6):
	    print("+---"*7 + "+")
	    for j in range(7):
	        print("| "+ col[i][j] + " ", end = "")
	    print("|")
	print("+---"*7 + "+")
	for num in range(7):
	    print("  " + str(num) + " ", end = "")

# --------------------Find-Winner-----------------------
#問題:col row寫相反
	for i in range (3, 6):
		for j in range (7):
			# print(i, j)
			if col[i][j] == col[i-1][j] == col[i-2][j] == col[i-3][j] \
            =="X":
				print("winner = X")
				done = True
			elif col[i][j] == col[i-1][j] == col[i-2][j] == col[i-3][j] \
            =="O":
				print("winner = O")
				done = True


    #horizontal
	for i in range(6):
		for j in range (3, 7):
			# print(i, j)
			if col[i][j] == col[i][j-1] == col[i][j-2] == col[i][j-3] \
				=="X":
				print("winner = X")
				done = True
			elif col[i][j] == col[i][j-1] == col[i][j-2] == col[i][j-3] \
				=="O":
				print("winner = O")
				done = True

    #diagonal(1)
	for i in range (3, 6):
		for j in range (3, 7):
			if col[i][j] == col[i-1][j-1] == col[i-2][j-2]== col[i-3][j-3]\
        	== "X":
				print("winner = X")
				done = True
			elif col[i][j] == col[i-1][j-1] == col[i-2][j-2]== col[i-3][j-3]\
        	== "O":
				print("winner = O")
				done = True
    #diagonal(2)
	for i in range (3):
		for j in range (3, 7):
			if col[i][j] == col[i+1][j-1] == col[i+2][j-2] == col[i+3][j-3]\
			== "X":
				print("winner = X")
				done = True
			elif col[i][j] == col[i+1][j-1] == col[i+2][j-2] == col[i+3][j-3]\
			== "O":
				print("winner = O")
				done = True

#檢查是否平局
	draw = True
	for i in range(6):
		for j in range(7):
			if " " in col[i][j]:
				draw = False
				break
	if draw == True:
		print("Draw")
		done = True

#p4
# 題意:
# 讓輸入的人輸日一塊矩陣pixel，程式要先看我給定的(x,y)是哪一個數字(顏色)
# 接著，要將這個數字相鄰的相同數字更改成輸入的變數k

# 想法:每走到一個地方:
# 1.檢查他的四周有沒有元素
# 2.把所有存在的位置都記錄在coor中
# 3.接著依序檢查，我們不需要設置一個位置變數i去讓他一個個檢查，因為只要delete掉就好了
# 4.當最後都處裡完，一個都不剩的時候，就跳出while迴圈
# 5.依行print出來


# -------------------------------------Replacing-number-in-a-matrix-------------------------------------
###======================replacing number in a matrix==============================
# <x, y> : target location

n = input('Enter index x, y, k (separate by whitespace): ')
n_list = n.split(' ')
X, Y, k = list(map(int, n_list))
print('Enter the matrix by multiple lines:')

matrix = []
while True:
    row = input().split(' ')
    if row == ['q']:
        break
    matrix.append(row)  # 保持矩陣元素為字符串類型

# 確認當前數值
color = matrix[X][Y]
color_revise = [[X, Y]]
k = str(k)  # 將 k 轉為字符串以便進行比較和賦值

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 包括對角線的8個方向

while color_revise:
    x, y = color_revise.pop(0)  # 使用 pop(0) 以進行 BFS

    if matrix[x][y] == color:
        matrix[x][y] = k

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == color:
                color_revise.append([nx, ny])

for row in matrix:
    print(' '.join(map(str, row)))


#p5
# ------------------------------Water-Filling---------------------------------------
# 檢測概念，從左邊出發向右邊去看

seats = input("Input sequence of seats: ").split()
seats = list(map(int, seats))

water = 0 #紀錄總共有多少water
r_max = [0] * len(seats)
l_max = [0] * len(seats)

i = 0
while i < len(seats):
	j = i
	#right_max
	while j < len(seats):
		if seats[j] >= seats[i] and seats[j] > r_max[i]:
			r_max[i] = seats[j]
		j +=1

	#left_max
	j = i
	while j >= 0:
		if seats[j] >= seats[i] and seats[j] > l_max[i]:
			l_max[i]= seats[j]
		j -=1
	water = water + min(l_max[i], r_max[i]) - seats[i]	
	#取左右最高的最小值，也就是說當前可以被填滿的最高高度，然後在減掉當前的高度，就是最終可以填滿的水量
	i +=1
print("water : ", water)


