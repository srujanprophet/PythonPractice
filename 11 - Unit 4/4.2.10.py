n = int(raw_input("Enter no. of rows of matrix : "))
m = int(raw_input("Enter no. of columns of matrix : "))

a=[[0 for row in range(n)]for col in range(m)]

sum = 0
for i in range(0,m):
    for j in range(0,n):
        a[i][j] = int(raw_input("Enter Element : "))
        if a[i][j] % 2 == 0:
            sum += a[i][j]

print sum

