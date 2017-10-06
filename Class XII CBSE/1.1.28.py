l = []
n = int(raw_input("Enter length of list : "))
for i in range (n):
    x = int(raw_input("Enter number : "))
    l.append(x)

y = int(raw_input("Enter element to search for : "))
temp = 1
for i in range(len(l)):
    if y == l[i]:
        print "Element found at index",i+1
        temp = 0


if temp == 1:
    print "Element not found"
