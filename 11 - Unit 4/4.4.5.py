t = tuple()
n = int(raw_input("Enter no. of customers : "))
for i in range(n):
    x = raw_input("Enter name of customer : ")
    t = t + (x,)

for i in range(n):
    print "Customer's Name - ",t[i]
