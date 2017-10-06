def myfun1(SL,x):
    for i in range(0,len(SL)):
        if SL[i] >= x:
            SL.insert(i,x)
            break
    print "Final List:",SL

def myfun2(SL,x):
    for i in range(0,len(SL)):
        if x == SL[i]:
            SL.remove(SL[i])
            break
    print "Final List:",SL

SL = []
n = int(raw_input("Enter length of Sorted List : "))
for i in range(n):
    y = int(raw_input("Enter Element : "))
    SL.append(y)
print "Initial List : ",SL
t = int(raw_input("Enter Number to be inserted : "))
myfun1(SL,t)
T = int(raw_input("Enter Number to be deleted : "))
myfun2(SL,T)


