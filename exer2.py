n = int(raw_input("Enter a number : "))

if ((n%2) == 0 ):
	print "Even Number"
else :
	print "Odd Number"

#Extra 1

if ((n%4) == 0 ):
	print "Divisible by 4"
else :
	print "Not Divisible by 4"

#Extra 2

x = int(raw_input("Enter Number to check  "))
y = int(raw_input("Enter Number to divide by "))

if ((x%y) == 0) :
	print x," divides ", y , "evenly"
else: 
	print x, " does not divide ", y , "evenly"



