from random import randint
from sys import exit
import os

OUT = [ "Bowled Him", "Edged and Gone", "High up in the air, Fielder coming underneath and takes the catch",
		"Finger goes up, LBW!", "Run Out :(", "Caught and bowled"
	]

##def Toss():
	
##	print "Choose heads or tails: (Press enter after deciding)."
##	raw_input("> ")
##	toss = randint(0,2)
##	if toss == 1:
##		print "It's heads, You are team 1."
##	else:
##		print "It's tails. You are team 2."


def Choose():
		print "Choose from the following formats of the game:\n "
		print "(a) Super Over\n(b) 2-Overs\n(c) 5-Overs\n"
		choice = raw_input("> ")
		
		if choice == "a":
			one_over()
				
		elif choice == "b":
			two_overs()
		
		elif choice == "c":
			five_overs()
		else:
			print "Type a,b or c"
			Choose()
		


def one_over(): 
		os.system('cls')
		print "-" * 15, "Super Over", '-' * 15, "\n"
		score1 = 0
		wkt1 = 0
		i = 1
		j =  1 * 6
		print team1, " Batting (Press Enter to Bat)\n"
		while i != j + 1 and wkt1 != 10:
			raw_input("> ")
			x = randint(0,6)
			if x == 0:
				y = randint(0,5)
				print OUT[y]
				wkt1 += 1
				i += 1
			elif x == 1:
				print "\nJust one Run.\n"
				score1 += 1
				i += 1
			elif x == 2:
				print "\nTwo Runs.\n"
				score1 += 2
				i += 1
			elif x == 3:
				print "\nThree Runs.\n"
				score1 += 3
				i += 1
			elif x == 4:
				print "\n4 RunsGlorious shot for an exquisite boundary!\n"
				score1 += 4
				i += 1
			elif x == 5:
				print "\nWell bowled. Dot ball\n"
				i += 1
			else:
				print "\nThat's gone miles. Miles! 6 Runs\n"
				score1 += 6
				i += 1
			print "The Score is : ", score1, "/", wkt1
			Balls(i) 
		print "\n", team1, score1, " / ", wkt1, "\n"
		raw_input("------------------ Innings Over -----------------------")
		k = 1
		score2 = 0
		wkt2 = 0
		print  "\n", team2, " Batting\n"
		while k != j + 1 and wkt2 != 10:
			raw_input("> ")
			x = randint(0,6)
			if x == 0:
				y = randint(0,5)
				print OUT[y]
				wkt2 += 1
				k += 1
			elif x == 1:
				print "\nJust one Run.\n"
				score2 += 1
				k += 1
			elif x == 2:
				print "\nTwo Runs.\n"
				score2 += 2
				k += 1
			elif x == 3:
				print "\nThree Runs.\n"
				score2 += 3
				k += 1
			elif x == 4:
				print "\n4 RunsGlorious shot for an exquisite boundary!\n"
				score2 += 4
				k += 1
			elif x == 5:
				print "\nWell bowled. Dot ball\n"
				k += 1
			else:
				print "\nThat's gone miles. Miles! 6 Runs\n"
				score2 += 6
				k += 1
			print "The Score is : ", score2, "/", wkt2, "\n"
			Balls(k)
			if score2 > score1:
				print team2, score2, " / " ,wkt2
				print "\n", team2, " is the winner!\n"
				exit(0)
			elif score2 <= score1: 
				pass
			else:
				exit(0)
		if score2 < score1:
			print team2, score2, " / " ,wkt2
			print "\n", team1, " is the Winner"
		else:
			print "\nIt's a Draw"
			
def two_overs():
		os.system('cls')
		print '-' * 15, "2-Over Match", '-' * 15, "\n"
		score1 = 0
		wkt1 = 0
		i = 1
		j =  2 * 6
		print "\n", team1, " Batting (Press Enter to Bat)\n"
		while i != j + 1 and wkt1 != 10:
			raw_input("> ")
			x = randint(0,6)
			if x == 0:
				y = randint(0,5)
				print OUT[y]
				wkt1 += 1
				i += 1
			elif x == 1:
				print "\nJust one Run.\n"
				score1 += 1
				i += 1
			elif x == 2:
				print "\nTwo Runs.\n"
				score1 += 2
				i += 1
			elif x == 3:
				print "\nThree Runs.\n"
				score1 += 3
				i += 1
			elif x == 4:
				print "\n4 Runs.Glorious shot for an exquisite boundary!\n"
				score1 += 4
				i += 1
			elif x == 5:
				print "\nWell bowled. Dot ball\n"
				i += 1
			else:
				print "\nThat's gone miles. Miles! 6 Runs\n"
				score1 += 6
				i += 1
			print "The Score is : ", score1, "/", wkt1
			Balls(i)
		print "\n", team1, score1, " / ", wkt1, "\n"
		raw_input("------------------ Innings Over -----------------------")
		k = 1
		score2 = 0
		wkt2 = 0
		print "\n", team2, "Batting\n"
		while k != j + 1 and wkt2 != 10:
			raw_input("> ")
			x = randint(0,6)
			if x == 0:
				y = randint(0,5)
				print OUT[y]
				wkt2 += 1
				k += 1
			elif x == 1:
				print "\nJust one Run.\n"
				score2 += 1
				k += 1
			elif x == 2:
				print "\nTwo Runs.\n"
				score2 += 2
				k += 1
			elif x == 3:
				print "\nThree Runs.\n"
				score2 += 3
				k += 1
			elif x == 4:
				print "\n4 Runs.Glorious shot for an exquisite boundary!\n"
				score2 += 4
				k += 1
			elif x == 5:
				print "\nWell bowled. Dot ball\n"
				k += 1
			else:
				print "\nThat's gone miles. Miles! 6 Runs\n"
				score2 += 6
				k += 1
			print "The Score is : ", score2, "/", wkt2, "\n"
			Balls(k)
			if score2 > score1:
				print "\n", team2, score2, " / " ,wkt2
				print "\n", team2, "is the winner!\n"
				exit(0)
			elif score2 <= score1: 
				pass
			else:
				exit(0)
		if score2 < score1:
			print "\n", team2, score2, " / " ,wkt2
			print "\n", team1,  "is the Winner"
		else:
			print "\nIt's a Draw!"
			
def five_overs():
		os.system('cls')
		print '-' * 15, "5-Over Match", '-' * 15
		score1 = 0
		wkt1 = 0
		i = 1
		j =  5 * 6
		print "\n", team1, "Batting (Press Enter to Bat)\n"
		while i != j + 1 and wkt1 != 10:
			raw_input("> ")
			x = randint(0,6)
			if x == 0:
				y = randint(0,5)
				print OUT[y]
				wkt1 += 1
				i += 1
			elif x == 1:
				print "\nJust one Run.\n"
				score1 += 1
				i += 1
			elif x == 2:
				print "\nTwo Runs.\n"
				score1 += 2
				i += 1
			elif x == 3:
				print "\nThree Runs.\n"
				score1 += 3
				i += 1
			elif x == 4:
				print "\n4 Runs.Glorious shot for an exquisite boundary!\n"
				score1 += 4
				i += 1
			elif x == 5:
				print "\nWell bowled. Dot ball\n"
				i += 1
			else:
				print "\nThat's gone miles. Miles! 6 Runs\n"
				score1 += 6
				i += 1
			print "The Score is : ", score1, "/", wkt1
			Balls(i)
		print "\n", team1, score1, " / ", wkt1, "\n"
		raw_input("------------------ Innings Over -----------------------")
		k = 1
		score2 = 0
		wkt2 = 0
		print "\n", team2, "Batting\n"
		while k != j + 1 and wkt2 != 10:
			raw_input("> ")
			x = randint(0,6)
			if x == 0:
				y = randint(0,5)
				print OUT[y]
				wkt2 += 1
				k += 1
			elif x == 1:
				print "\nJust one Run.\n"
				score2 += 1
				k += 1
			elif x == 2:
				print "\nTwo Runs.\n"
				score2 += 2
				k += 1
			elif x == 3:
				print "\nThree Runs.\n"
				score2 += 3
				k += 1
			elif x == 4:
				print "\n4 Runs.Glorious shot for an exquisite boundary!\n"
				score2 += 4
				k += 1
			elif x == 5:
				print "\nWell bowled. Dot ball\n"
				k += 1
			else:
				print "\nThat's gone miles. Miles! 6 Runs\n"
				score2 += 6
				k += 1
			print "The Score is : ", score2, "/", wkt2, "\n"
			Balls(k)
			if score2 > score1:
				print "\n", team2, score2, " / " ,wkt2
				print "\n", team2, "is the winner!\n"
				exit(0)
			elif score2 <= score1: 
				pass
			else:
				exit(0)
		if score2 < score1:
			print "\n", team2, score2, " / " ,wkt2
			print "\n", team1, "is the Winner"
		else:
			print "\nIt's a Draw!"
			
			
def Balls(b):
		u = b - 1
		print "Overs: ", u/6, ".", u%6, "\n"
	
def Start():
	print "************** Welcome to The Classic 2-Player Game of Book Cricket **************"
	
##	Toss()
	Choose()

print "Enter name of team 1: "	
team1 = raw_input()	
print "Enter name of team 2: "
team2 = raw_input()

##def Score1(x):
##	team1 = x
##	return x

##def Score2(y):
##	team2 = y
##	return y

Start()

print "---------------------------------------------------"
print "\n\nThanks for Playing!" 