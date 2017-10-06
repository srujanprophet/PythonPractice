from random import randint
from sys import exit

print "\n", '-' * 25, "Virtual Dice", '-' * 25

def one_dice():
	x = randint(1,6)
	print "You get :", x
	print "Press Enter to go again or press 'q' to Exit"
	resp = raw_input("> ")
	if resp == "q":
		exit(0)
	else:
		one_dice()
		
def two_dice():
	x = randint(1,6)
	y = randint(1,6)
	print "Dice 1: ", x, "\tDice 2: ", y
	print "You get: ", x + y
	print "Press Enter to go again or press 'q' to Exit"
	resp = raw_input("> ")
	if resp == "q":
		exit(0)
	else:
		two_dice()
		
def three_dice():
	x = randint(1,6)
	y = randint(1,6)
	z = randint(1,6)
	print "Dice 1: ", x, "\tDice 2: ", y, "\tDice 3: ", z
	t = x + y + z
	print "You get: ", t
	print "Press Enter to go again or press 'q' to Exit"
	resp = raw_input("> ")
	if resp == "q":
		exit(0)
	else:
		three_dice()
		
def Menu():
	print "Choose no. of dice (max. is 3) : "
	resp = raw_input("> ")
	if resp == "1":
		one_dice()
	elif resp == "2":
		two_dice()
	else:
		three_dice()
		


print "\nDeveloped by srutek engine. Trademark and copyright to srutek ltd.\n "
print '*' * 60, "\n"
Menu()
