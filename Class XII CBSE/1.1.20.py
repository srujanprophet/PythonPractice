n = int(raw_input("Enter Number : "))
sum = 0
while n > 0:
    x = n % 10
    sum += x
    n = n/10

print "Sum of digits : ",sum
