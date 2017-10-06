#Used costumers instead of "lists"

customers = dict()
n = int(raw_input("Enter no. of customers : "))
for i in range(n):
    a = raw_input("Enter Name : ")
    b = raw_input("Enter Phone No. : ")
    customers[a] = b

x = raw_input("Enter Name : ")
l = customers.keys()

for i in l:
    if i == x:
        print customers[i]
    else:
        print "Name not in list. Sorry !"

