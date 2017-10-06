from random import randint

def roll_D(x=6,y=1):
    for i in range(0,y):
        z = randint(1,x)
        print z

a = int(raw_input("Enter no. of faces : "))
b = int(raw_input("Enter number of dice to roll : "))

roll_D(a,b)
