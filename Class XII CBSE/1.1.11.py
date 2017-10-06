t = int(raw_input("Enter any Number : "))
n = t
sum = 0
while n > 0:
    x = n%10
    sum += x**3
    n = n/10

if sum == t:
    print "It is an armstrong number"

else:
    print "It is not an armstrong number"
