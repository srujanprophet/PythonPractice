z1r = int(raw_input("Enter real part of 1st complex no. :"))
z1i = int(raw_input("Enter imaginary part of 1st complex no. :"))
z2r = int(raw_input("Enter real part of 2nd complex no. :"))
z2i = int(raw_input("Enter imaginary part of 2nd complex no. :"))

Zr = z1r*z2r - z1i*z2i
Zi = z1r*z2i + z1i*z2r

print "Multiplication of these two complex no. yields"
print Zr,'+','i',Zi
