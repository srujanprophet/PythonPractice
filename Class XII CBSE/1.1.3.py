t = tuple()
T = tuple()
i = 5
while i < 101:
    t = t + (i,)
    i += 5
print t

j = 100
while j > 1:
    T = T + (j,)
    j -= 2

print T
