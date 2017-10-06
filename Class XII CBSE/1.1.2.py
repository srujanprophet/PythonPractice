t = tuple()
T = tuple()
for i in range(0,301,10):
    t = t + (i,)
print t
for i in range(105,6,-7):
    T = T + (i,)
print T

fact = 1.0
for i in range(365,296,-1):
    fact = fact*i

x = 365.0**68.0
ans = ((fact/x))
print ans
