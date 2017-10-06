def selectionsort( aList ):
  for i in range( len( aList ) ):
    least = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] > aList[least]:
        least = k

    swap( aList, least, i )

  return aList

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp


l = []
n = int(raw_input("Enter No. of Students:"))
for i in range(n):
    r = raw_input("Enter Roll No.:")
    l.append(r)
    n = raw_input("Enter Name :")
    l.append(n)
    m = raw_input("Enter Marks :")
    l.append(m)

marks = l[2::3]
new = selectionsort(marks)
