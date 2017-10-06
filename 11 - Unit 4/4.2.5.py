def remove_duplicates(l):
    L = []
    for i in l:
        if i not in L:
            L.append(i)
    return L

n = int(raw_input("Enter length of list : "))
print "Enter elements of list -"
x = []
for i in range(0,n):
    y = int(raw_input("Enter number : "))
    x.append(y)

print remove_duplicates(x)

