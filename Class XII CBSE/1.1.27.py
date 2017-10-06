l = []
n = int(raw_input("Enter length of list : "))
for i in range (n):
    x = int(raw_input("Enter number : "))
    l.append(x)

temp = int(raw_input("Enter Number to be inserted : "))
y = int(raw_input("Enter position at which it is to be inserted : "))

l.insert(y,temp)
print l
