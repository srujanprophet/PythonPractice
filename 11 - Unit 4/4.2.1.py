
coeff = [-13.39,17.5,3.0,0,1.0]
x = float(raw_input("Enter value of x : "))
sum = 0
for i in range(0,len(coeff)):
   sum += coeff[i]*(x**i)

print sum


