#p1
for theif in range(1, 5):
	if ((1 !=theif)+(3 == theif)+(4 == theif)+(4 != theif)==3):
		print("the theif is ", theif)
	else:
		continue
#p2
#Finding perfect numbers
n = int(input("Please input the range number:"))
num = 2 	#from 2 to n，so starting form n
print("Perfect numbers:")
while num <= n:	#range 的確定
	divisors_sum = 0 	#先假設要檢測的這個值總合為0
	i = 1 	#檢測是否為因數，從1開始
	while i < num: 	#做因數的檢定迴圈
		if num % i == 0: 	#如果整除
			divisors_sum = divisors_sum + i 	#他就會被加入因數和
		i = i + 1	#此時被檢測的因數也要隨之+1
	if divisors_sum == num: 	#當符合perfect number的條件時
		print(num)
	num += 1 	#繼續檢測下一個數字

#p3
#-----------------------------------輸入年分--------------------------------------------------
year = int(input("input Year:"))
month = int(input("input month:"))
#-----------------------------------判斷是否為閏年--------------------------------------------
is_leap_year = year % 4 == 0 and (year%100 !=0 or year%400 ==0)

#---------------------------------判斷month裡面有幾天------------------------------------------

days_in_month = 31
if month ==2:
	if is_leap_year:
		days_in_month = 29
	else:
		days_in_month = 28
elif month in [4, 6, 9, 11]: #錯誤點:這邊不可以用month == [4, 6, 9, 11]，因為它是一個屬於list裡面的值
	days_in_month = 30

#---------------------------------算當年當月的1號是星期幾-------------------------------------------
if month <= 2:
	a = (year-1)//100
	b = (year-1)%100
	# b =(year-1)-(a*100)
	month = month + 10
else:
	a = year//100
	b = year%100
	month = month - 2



formula = (1 + int(2.6 * month - 0.2) - 2*a + b + a//4 + b//4) % 7
# 註解:在這邊計算formula公式的時候有可能出現負數的情形，要調整成負數
if formula < 1:
	formula += 7



#-------------------------------------列印出星期幾----------------------------------------------------
print("Sun Mon Tue Wed Thu Fri Sat")

start_day = 1 #從一號開始
while start_day <= days_in_month:
	i = 0
	while i < 7:
		if i < formula:
			print("   ", end = " ")
		else:
			print(" " + "{:02}".format(start_day), end=" ") #我自己在想，因為字串長度是3，可是我如果寫成單純只影02，前面沒有空格的時候，他就會格式跑掉，所以加一個空格對排版會比較好看
			start_day = start_day + 1
			if start_day > days_in_month:
				break
		i += 1
	
	print()
	formula = 0 #讓第一周輪完之後就不要再進入到if的判斷了

#p4
layer= int(input("Enter the number of layers(2 to 5)="))
length=int(input("Enter the side length of the top layer(2 to 6)="))
growth=int(input("Enter the growth of each layer(1 to 5)="))
t_width=int(input("Enter the trunk width(odd number, 3 to 9)="))
t_height=int(input("Enter the trunk height(4 to 10)="))


x=length+growth*(layer-1)-1#x為最後一層最後一行的＃個數(去掉中間只有單邊)
print(" "*x + "#")#先列出第一層第一行的＃

a=0#a為增加的層數
while a<=(layer-1):#利用迴圈，a每一次加一，就算出每一層的圖案
	p=1
	#扣除每一層的第一行和最後一行，其餘每一行＠的數量為(2*p-1)，且其餘每一行最左邊的空格為(x-p)
	q=length+growth*a #在每一次循環中，首先計算出當前層的行數 q，然後進入內層 while 迴圈來處理該層的每一行
	while p<=q-2: 
	#因為＠只出現在每一層扣除第一行和最後一行的其他行，所以p最大值為q-2
		print(" "*(x-p)+"#" + "@"*(2*p-1) + "#")
		p=p+1
	
	print(" "*(x-p)+"#"*(2*p+1))#印出每一層最後一行的＃個數
	a=a+1


b=int((t_width-1)/2)#b為樹幹寬度中心對稱，單邊｜的個數
print((" "*(x-b)+"|"*t_width+"\n")*t_height)#左邊空格為(x-b)格


#p5
#----------------Part-1-Fibonacci-Sequence-------------------------------
n = input_num = int(input("Input an interger number:"))
#---------------------進入迴圈------------------------------------------------
def f(x): 	#使用定義函數的方法
	if x == 1 or x == 2: 	#前兩項(不討論0)都是1
		return 1	#賦予( f(x) )值1
	else:
		return f(x-1) + f(x-2)

fib_n = f(n)
print("the", n,"-th Fibonacci number is :" , fib_n)

#===================================原始只判斷最長的那個的程式=====================================================
start = 0 	#初始的字串從0開始跑
max_length = 0
# ---------------------------奇數判斷--------------------------------------------
for i in range(len(string)):
	left = i
	right = i
# ---------------------------While1---------------------------------------------
	while left >= 0 and right< len(string) and string[left] == string[right]:
		#註解:只要沒有進入到if迴圈當中，start的起始點位置就不會被更換
		if right - left + 1 > max_length:
			max_length = right - left + 1
			start = left
		left = left - 1
		right = right + 1

# ------------------------------偶數判斷-----------------------------------
for i in range(len(string)): 	#這邊判斷的是這個位置的字符和他後面那個去做比較
	left = i
	right = i + 1
#---------------------------While2(在迴圈2裡面，只要在一開始左右比較不相等->直接break)----------------
	while left>=0 and right< len(string) and string[left] == string[right]:
		if right - left + 1 > max_length:
			max_length = right - left + 1
			start = left
		left = left - 1
		right = right + 1
longest_Palindromic = string[start:start + max_length]
length = len(longest_Palindromic)
print("the length of longest Palindromic is :", length)
print("the longest Palindromic substring is :", longest_Palindromic)

# ---------------------------------想法----------------------------------------------------
# 先把12輸近來統整成公式

#====================================input==================================================
n = Fibonacci = int(input("the number of the requested element if Fibonacci(n) = "))
first_string = input("the first string for Palindromic detection (s1) = ")
second_string = input("the second string for Palindromic detection (s2) = ")
Plaintext = input("the Plaintext to be encrypted : ")

#================================Part-1-Fibonacci-Sequence============================================
# n = input_num = int(input("Input an interger number:"))
#-------------------------------進入迴圈------------------------------------------------
print("------------------exact key for encrypted method-----------------------")

def f(x):
	if x == 1 or x == 2:
		return 1
	else:
		return f(x-1) + f(x-2)

fib_n = f(n)
print("the", n,"-th Fibonacci number is :" , fib_n)

#=============================Part-2-Longest-Palindromic-substring=======================================
# string = input("Enter a string:")

start = 0
max_length = 0

# ---------------------------first_string_judge--------------------------------------------


for i in range(len(first_string)):
	left = i
	right = i
# ---------------------------While1---------------------------------------------
	while left >= 0 and right< len(first_string) and first_string[left] == first_string[right]:
		if right - left + 1 > max_length:
			max_length = right - left + 1
			start = left
		left = left - 1
		right = right + 1

# ------------------------------偶數判斷-----------------------------------
for i in range(len(first_string)):
	left = i
	right = i + 1
#---------------------------While2(在迴圈2裡面，只要在一開始左右比較不相等->直接break)----------------
	while left>=0 and right< len(first_string) and first_string[left] == first_string[right]:
		if right - left + 1 > max_length:
			max_length = right - left + 1
			start = left
		left = left - 1
		right = right + 1
longest_Palindromic = first_string[start:start + max_length]
a = longgest_length = len(longest_Palindromic)
print("the longest Palindromic within first string is :", longest_Palindromic)
print("length is :", longgest_length)

# --------------------------------second_string_judge--------------------------------------------

start = 0
max_length = 0

for i in range(len(second_string)):
	left = i
	right = i
# ---------------------------While1---------------------------------------------
	while left >= 0 and right< len(second_string) and second_string[left] == second_string[right]:
		if right - left + 1 > max_length:
			max_length = right - left + 1
			start = left
		left = left - 1
		right = right + 1

# ------------------------------偶數判斷-----------------------------------
for i in range(len(second_string)):
	left = i
	right = i + 1
#---------------------------While2(在迴圈2裡面，只要在一開始左右比較不相等->直接break)----------------
	while left>=0 and right< len(second_string) and second_string[left] == second_string[right]:
		if right - left + 1 > max_length:
			max_length = right - left + 1
			start = left
		left = left - 1
		right = right + 1
second_longest_Palindromic = second_string[start:start + max_length]
b = second_length = len(second_longest_Palindromic)
print("the longest Palindromic within second string is :", second_longest_Palindromic)
print("length is :", second_length)

print("---------------------------encrypted completed-----------------------")

# =======================================Part-3===================================================
# print(a, b)

#-----------------------------------公式---------------------------------------------

word = Plaintext
# 定義list

encripted_chars = []
encripted_chars_to_num = []
encripted_chars_to_num_cal = []
correspond_chars_from_ASCll = []

for char in word:
	x1 = ord(char)
	y1 = x1 + fib_n
	encripted_chars.append(y1)
	y2 = a * y1 + b
	encripted_chars_to_num.append(y2)
	y3 = (y2 - 65) % 26 + 65
	encripted_chars_to_num_cal.append(y3)
	y4 = chr(y3)
	correspond_chars_from_ASCll.append(y4)


# print(encripted_chars)
# print(encripted_chars_to_num)
# print(encripted_chars_to_num_cal)
# print(correspond_chars_from_ASCll)
result_str = ''.join(correspond_chars_from_ASCll)
print("the encrypted text is:", result_str)






