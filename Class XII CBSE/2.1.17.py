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

def insertionsort( aList ):
  for i in range( 1, len( aList ) ):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp

l = []
n = int(raw_input("Enter No. of Items:"))
for i in range(n):
    ic = raw_input("Enter Item Code:")
    l.append(ic)
    In = raw_input("Enter Item Name :")
    l.append(In)
    p = raw_input("Enter Price :")
    l.append(p)

price = l[2::3]
bubblesort(price)

