x = raw_input("Enter Number in Binary : ")
sum = 0
y = x[::-1]
l = len(x)
for i in range(l):
    z = int(y[i])
    t = z*(2**i)
    sum += t

print "Number in Decimal is ",sum
