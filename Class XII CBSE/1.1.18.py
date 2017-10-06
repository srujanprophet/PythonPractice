f1 = raw_input("Enter First Distance (x'y\") : ")
f2 = raw_input("Enter Second Distance (x'y\") : ")

F1 = (float(f1[0])*12 + float(f1[1]))*2.54
F2 = (float(f2[0])*12 + float(f2[1]))*2.54

F = F1 + F2

i = F*0.3937008
j = i/12.0
k = (j%1)*12

print
x = int(j)
y = int(k)

print "Sum of distances is",x,'\'',y,'\"'

