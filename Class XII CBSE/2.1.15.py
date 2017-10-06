def selectionsort( aList ):
  for i in range( len( aList ) ):
    least = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] < aList[least]:
        least = k

    swap( aList, least, i )
    
  print aList

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp


l = []
n = int(raw_input("Enter No. of Students:"))
for i in range(n):
    x = raw_input("Enter Name of Students:")
    l.append(x)

selectionsort(l)

