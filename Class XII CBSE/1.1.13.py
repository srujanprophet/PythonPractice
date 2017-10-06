n = int(raw_input("Enter Number : "))
print "Prime number(s) upto ",n,' are'
print 2

def isprime(x):
    temp = 0
    for j in range(2,x):
        if x%j == 0:
            temp = 0
            break
        else:
            temp = 1
    return temp

for i in range(2,n+1):
    t = isprime(i)
    if t == 1:
        print i
