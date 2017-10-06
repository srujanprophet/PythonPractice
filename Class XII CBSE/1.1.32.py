l = []
n = int(raw_input("Enter n :"))
for i in range(n):
    x = int(raw_input("Enter number : "))
    l.append(x)

print "Set of Numbers :",l
print "Reversed set of Numbers",l[::-1]
