from sys import exit

def start():
	print "----- Welcome to the Carnival of Horrors! -----"
	print "You find yourself at the fence, what do you do?"
	print "go home or climb fence"
	resp1 = raw_input("> ")
	if resp1 == "go home":
		print "Come on! Really?"
		exit(0)
	elif resp1 == "climb fence":
		climbed()
	else:
		print "No can't do baby doll!"
	
def climbed():
	print "You enter the carnival and find it completely uninhabited."
	print "There are rides and their are games. What will you try first?"
	resp2 = raw_input("> ")
	if resp2 == "rides":
		riding()
	elif resp2 == "games":
		games()
	else:
		print "Not an option!"
		
def riding():
	print "You get in the car. Where do you want to go?"
	print "house of horrors or go back"
	resp3 = raw_input("> ")
	if resp3 == "house of horrors":
		print "Bam! your car detaches and you are stuck in the crash"
		print "Two men pick your rigid body and put it up for display."
		print "You are a dummy now, literally. Good job!"
	elif resp3 == "go back":
		print "Man up, don't pull out!"
		start()
	else:
		print "Type English."

def games():
	print "You find a diamond the size of a tangerine on the car."
	print "What do you do? Take it or Leave it?"
	resp4 = raw_input("> ")
	if resp4 == "take":
		print "Fast forward 2 months. chiling out in heaven or hell whatever!"
	elif resp4 == "leave":
		print "Some things are just meant to be. Kudos on not being greedy. You win and make out of it alive."
	else:
		print "Do something . Dammit!"

start()