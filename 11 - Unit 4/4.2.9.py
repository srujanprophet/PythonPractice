def product(l):
    x = 1
    for i in range(0,len(l)):
        x *= l[i]

    return x

n = int(raw_input("Enter length of list : "))
print "Enter elements of list (numbers only) -"
x = []
for i in range(0,n):
    y = int(raw_input("Enter number : "))
    x.append(y)

print product(x)
