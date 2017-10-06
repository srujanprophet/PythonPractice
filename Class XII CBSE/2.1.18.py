def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] < A[k - 1] ):
        swap( A, k, k - 1 )
  print A

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

l = []
n = int(raw_input("Enter length of list:"))
for i in range(n):
    x = int(raw_input("Enter Element :"))
    l.append(x)

bubblesort(l)
temp = int(raw_input("Enter Element for Position :"))
flag = 0
for j in range(n):
    if l[j] == temp:
        print "Position of Element :",j+1
        flag = 1


if flag == 0:
    print "Element not Found"
