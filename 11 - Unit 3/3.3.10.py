from random import randint

N = int(input("Enter N: "))
for i in range(0,N):
    x = randint(0,1)
    if x == 1:
        print("Tails")
    else:
        print("Heads")

