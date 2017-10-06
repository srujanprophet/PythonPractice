def binary_search(SL,x):
    low=0
    high=len(SL)-1
    while(low<high):
        mid=((low+high)/2)
        if SL[mid]== x:
            print "Element found at"
            print mid+1
            break
        if SL[mid]<x:
            low=mid+1
        if SL[mid]>x:
            high=mid-1
        if low >= high:
            print "ELEMENT NOT FOUND"

l = []
n = int(raw_input("Enter length of Sorted List:"))
for i in range(n):
    x = int(raw_input("Enter Element:"))
    l.append(x)
print l
t = int(raw_input("Enter Element to search for : "))
binary_search(l,t)

