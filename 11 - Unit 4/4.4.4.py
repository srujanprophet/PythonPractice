t = tuple()
n=input("Total number of values in tuple")
for i in range(n):
    a=input("enter elements")
    t=t+(a,)
print "maximum value=",max(t)
print "minimum value=",min(t)
