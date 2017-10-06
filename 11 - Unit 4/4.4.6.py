t = tuple()
n = int(raw_input("Enter length of tuple :"))
for i in range(n):
    x = int(raw_input("Enter Element : "))
    t = t + (x,)

T1 = t[::2]
T2 = t[1::2]

print T1,'\n',T2
