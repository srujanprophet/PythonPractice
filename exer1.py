"""Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

name = raw_input("Enter your name : ")
age = int(raw_input("Enter your age : "))
century = (2016-age) + 100
x = int(raw_input("Enter no. of copies you want : "))
print x*(name + ', You will turn a 100 years old in the year ',century)
