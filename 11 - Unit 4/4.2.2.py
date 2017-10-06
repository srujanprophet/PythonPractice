def cumsum(l):
    sum = 0
    L = []
    for i in range(0,len(l)):
        sum += l[i]
        L.append(sum)
    return L

n = int(raw_input("Enter length of list : "))
print "Enter elements of list -"
x = []
for i in range(0,n):
    y = int(raw_input("Enter number : "))
    x.append(y)

print cumsum(x)
