T1 = tuple()
T2 = tuple()
n = int(raw_input("Enter length of tuple 1 : "))
k = int(raw_input("Enter length of tuple 2 :"))

print "         TUPLE 1         "
for i in range(n):
    x = int(raw_input("Enter element : "))
    T1 = T1 + (x,)

print "         TUPLE 2         "
for j in range(k):
    y = int(raw_input("Enter element : "))
    T2 = T2 + (y,)

if cmp(T1,T2) == 0:
    print "Both are same"

elif cmp(T1,T2) == 1:
    print "First Tuple is bigger"

else:
    print "Second Tuple is bigger"

