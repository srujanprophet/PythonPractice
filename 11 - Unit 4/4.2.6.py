def merge(l1,l2):
    l = []
    for i in range(0,len(l1)):
        l.append(l1[i])
    for j in range(0,len(l2)):
        l.append(l2[j])
    return l

print "Enter two sorted lists \n        LIST 1      "
n = int(raw_input("Enter length of list : "))
if n != 0:
    print "Enter elements of list - "
    x = []
    for i in range(0,n):
        t = int(raw_input("Enter number : "))
        x.append(t)
else:
    x = []

print "     LIST 2      "
n = int(raw_input("Enter length of list : "))
if n != 0 :
    print "Enter elements of list -"
    z = []
    for i in range(0,n):
        y = int(raw_input("Enter number : "))
        z.append(y)
else:
    z = []

print merge(x,z)
