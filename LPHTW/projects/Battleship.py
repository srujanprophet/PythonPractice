from random import randint

def foo():
	menu()
	
def QG():
	board = []

	for x in range(5):
		board.append(["O"] * 5)
		
	def print_board(board):
		for row in board:
			print " ".join(row)
	 
	print "Let's play Battleship!"
	print "You have 11 chances"
	print_board(board)
		
	def random_row(board):
		return randint(1, len(board) - 1)
	
	def random_col(board):
		return randint(1, len(board[0]) - 1)
	
	ship_row = random_row(board)
	ship_col = random_col(board)
		
	print ship_row
	print ship_col

	for turn in range(1,11):
	
		guess_row = int(raw_input("Guess Row:")) 
		guess_col = int(raw_input("Guess Col:"))
	
		if guess_row - 1 == ship_row and guess_col - 1 == ship_col:
			print "Congratulations! You sunk my battleship!"
			break
		else:
			if guess_row - 1 not in range(5) or guess_col - 1 not in range(5):
				print "Oops, that's not even in the ocean."
	        	elif(board[guess_row - 1][guess_col - 1] == "X"):
		        	print "You guessed that one already."
		        else:
		        	print "You missed my battleship!"
		        	board[guess_row - 1][guess_col - 1] = "X"
		        
		print "Turn", turn + 1
		print_board(board)
		if turn == 10:
			print "Game Over"


board = []
for x in range(7):
	board.append(["O"] * 7)
			
def print_board(board):
	for row in board:
		print " ".join(row)


def submarine():
	hole1 = []
	hole2 = []
		
	x = randint(0,6)
	y = randint(0,6)
		
	hole1.append(x)
	hole1.append(y)

	i = randint(0,1)
	if i == 0:
		if x < 7:  
			x1 = hole1[0] + 1
			y1 = hole1[1]
			hole2.append(x1) 
			hole2.append(y1)
		else:
			x1 = hole[0] - 1
			y1 = hole1[1]	
			hole2.append(x1) 
			hole2.append(y1)

	else:
		if y < 7:
			x1 = hole1[0]
			y1 = hole1[1] + 1
			hole2.append(x1)
		 	hole2.append(y1)
		else:
			x1 = hole1[0]
			y1 = hole1[1] - 1
			hole2.append(x1)
			hole2.append(y1)
		
	submarine_holes = hole1 + hole2
	return submarine_holes	
		
	
submarine_points = submarine()

sm_hole1 = submarine_points[0:2]
sm_hole2 = submarine_points[2:4]

def battleship():
	hole1 = []
	hole2 = []
	hole3 = []

	x = randint(0,6)
	y = randint(0,6)

	hole1.append(x)
	hole1.append(y)
	
	i = randint(0,1)
	if i == 0:
		if x < 6:  
			x1 = hole1[0] + 1
			y1 = hole1[1]
			hole2.append(x1) 
			hole2.append(y1)
			hole3.append(x1 + 1)
			hole3.append(y1)
		else:
			x1 = hole1[0] - 1
			y1 = hole1[1]	
			hole2.append(x1) 
			hole2.append(y1)
			hole3.append(x1 - 1)
			hole3.append(y1)
	
	else:
		if y < 7:
			x1 = hole1[0]
			y1 = hole1[1] + 1
			hole2.append(x1)
			hole2.append(y1)
			hole3.append(x1)
			hole3.append(y1 + 1)
		else:
			x1 = hole1[0]
			y1 = hole1[1] - 1
			hole2.append(x1)
			hole2.append(y1)
			hole3.append(x1)
			hole3.append(y1 - 1) 

	battleship_holes = hole1 + hole2 + hole3
	return battleship_holes

while True:
	battleship_points = battleship()
	bs_hole1 = battleship_points[0:2]
	bs_hole2 = battleship_points[2:4]
	bs_hole3 = battleship_points[4:6]
	if bs_hole1 != sm_hole1 and bs_hole1 != sm_hole2 and bs_hole2 != sm_hole1 and bs_hole2 != sm_hole2 and bs_hole3 != sm_hole1 and bs_hole3 != sm_hole2:
		break	


# print sm_hole1, '', sm_hole2
# print bs_hole1, '', bs_hole2, '', bs_hole3

def play():
	submarine = "Safe"
	battleship = "Safe"
	for turn in range(20):
		row = int(raw_input("> Enter row: "))
		col = int(raw_input("> Enter column: "))
		if ((row - 1) == sm_hole1[0] and (col - 1) == sm_hole1[1]) or ((row - 1) == sm_hole2[0] and (col - 1) == sm_hole2[1]):
			print "You hit the Submarine! "
			board[row - 1][col - 1] = "S"
		elif ((row - 1) == bs_hole1[0] and (col - 1) == bs_hole1[1]) or ((row - 1) == bs_hole2[0] and (col - 1) == bs_hole2[1]) or ((row - 1) == bs_hole3[0] and (col - 1) == bs_hole3[1]):
			print "You hit the Battleship! "
			board[row - 1][col - 1] = "S"
		else:
			if (row - 1 not in range(0,7) or col - 1 not in range(0,7)):
				print "Not in range!, Missed Completely"
			elif board[row - 1][col - 1] == "X":
				print "Shot there already"
			else:
				print "Missed!"
				board[row - 1][col - 1] = "X"
		print "Turn : ", turn + 2
		print_board(board)
		if board[sm_hole1[0]][sm_hole1[1]] == "S" and board[sm_hole2[0]][sm_hole2[1]] == "S" and submarine == "Safe":
	 		print "You have sunk the submarine. Good Job!"	
			submarine = "Sunk"
		elif board[bs_hole1[0]][bs_hole1[1]] == "S" and board[bs_hole2[0]][bs_hole2[1]] == "S" and board[bs_hole3[0]][bs_hole3[1]] == "S" and battleship == "Safe":
	 		print "You have sunk the battleship. Good Job!"		
			battleship = "Sunk"
		else:
			pass
		
		if battleship == "Sunk" and submarine == "Sunk":
			print "You Win ! "
			break
		if turn == 19:
			print "Game Over!"
	
			 
def menu():	
	print '-' * 10, "Let's Play Battleship", '-' * 10
	print "1. Quick Game\n2. Campaign\n3. Exit"
	print '-' * 43
	choice = int(raw_input("> Choose your option: "))
	while True:
		if choice == 1:
			QG()
			foo()
			break
		elif choice == 2:	
			print_board(board)
			play() 
			foo()
			break
		elif choice == 3:
			print "Thanks for Playing"
			break
		else:
			print "Invalid choice :( "
			foo()

foo()


