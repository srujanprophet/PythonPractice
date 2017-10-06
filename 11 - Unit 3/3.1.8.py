from math import sqrt

print "------ Solve any Quadratic (ax^2 + bx + c = 0) ------"
a = int(raw_input("Enter a : "))
b = int(raw_input("Enter b : "))
c = int(raw_input("Enter c : "))

D = b*b - 4*a*c
if D >= 0:
    x1 = (-b + sqrt(D))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)

    print "Roots of the equation are ",x1, " and ",x2

else:
    print "Non-Real Roots"
