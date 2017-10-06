d = dict()
n = int(raw_input("Enter no. of customers : "))
for i in range(n):
    a = raw_input("Enter customer name : ")
    b = raw_input("Enter customer phone no. : ")
    d[a] = b

temp = raw_input("Enter Customer Name to search : ")
k = 0
for x in d:
    if temp == x:
        print "Customer Phone No. ",d[x]
        k = 1
        break


if k == 0:
    print "Customer not found"
