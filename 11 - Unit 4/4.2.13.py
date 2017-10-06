m = int(raw_input("Enter no. of rows : "))
n = int(raw_input("Enter no. of columns : "))

a = [[0 for row in range(n)]for col in range(m)]

for i in range(0,m):
    for j in range(0,n):
        a[i][j] = int(raw_input("Enter Element : "))

rowsum = []
colsum = []
for k in range(0,m):
    rowsum.append(0)
for l in range(0,n):
    colsum.append(0)

for i in range(n):
    for j in range(m):
        colsum[i] += a[j][i]

for i in range(m):
    for j in range(n):
         rowsum[i] += a[i][j]

print "Row-wise sum : ", rowsum
print "Column-wise sum : ", colsum
