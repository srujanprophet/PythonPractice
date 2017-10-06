customers = dict()
n = int(raw_input("Enter no. of customers : "))

for i in range(n):
    a = raw_input("Enter Customer Name : ")
    b = raw_input("Enter Customer's Phone No. : ")
    customers[b] = a

name = raw_input("Enter Number of entry : ")
del customers[name]

print customers
