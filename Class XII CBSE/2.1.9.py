l = []
n = int(raw_input("Enter length of list:"))
for i in range(n):
    x = int(raw_input("Enter Element:"))
    l.append(x)
print l
N = int(raw_input("Enter Element for position: "))
flag = 0
for j in range(n):
    if N == l[j]:
        print "Element found at position",j+1
        flag = 1
        break
if flag == 0:
    print "Element not found."
