n = int(raw_input("Enter order of matrix : "))

a = [[0 for row in range(n)]for col in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = input("Enter element :")

for i in range(n):
    for j in range(n):
        if j < i :
            a[j][i] = 0


print "Lower Triangle Matrix is"
for i in range(n):
    for j in range(n):
        print a[i][j],'                ',
    print

