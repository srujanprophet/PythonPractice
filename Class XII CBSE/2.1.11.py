def insertion_sort(DATA_LIST):
    for K in range (1, len(DATA_LIST)):
        temp=DATA_LIST[K]
        ptr=K-1
        while(ptr>=0) and DATA_LIST[ptr]>temp:
            DATA_LIST[ptr+1]=DATA_LIST[ptr]
            ptr=ptr-1
        DATA_LIST[ptr+1]=temp
        print DATA_LIST
    print "Sorted List :",DATA_LIST
    
l = []
n = int(raw_input("Enter length of list to be sorted :"))
for i in range(n):
    x = int(raw_input("Enter Element:"))
    l.append(x)
print "Unsorted List:",l
insertion_sort(l)
