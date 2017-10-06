def is_sorted(l):
    temp = 0
    for i in range(0,len(l)-1):
        for j in range(len(l)-i-1):
            if l[i] > l[i+1]:
                temp = 1
                break
    if temp == 1:
        return False
    else:
        return True

n = int(raw_input("Enter length of list : "))
print "Enter elements of list -"
x = []
for i in range(0,n):
    y = int(raw_input("Enter number : "))
    x.append(y)

print is_sorted(x)
