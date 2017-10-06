import os
from pickle import dump,load

str = "This is how you remind me"
word = raw_input("Enter value to be deleted : ")
given = open("Givenfile.txt",'wb')
dump(str,given)
given.close()
given = open("Givenfile.txt",'rb')
temp = open("Temp.txt",'wb')

try :
    while True:
        x = load(given)
        X = x.split()
        t = []
        for i in range(len(X)):
            if word == X[i]:
                print "\n"
            else:
                t.append(X[i])
        dump(t,temp)
except EOFError:
    pass

temp.close()
temp = open("Temp.txt",'rb')
try :
    while True:
        Y = load(temp)
        final = ""
        for i in range(len(Y)):
            final = final + Y[i] + " "
        print final
except EOFError:
    pass
