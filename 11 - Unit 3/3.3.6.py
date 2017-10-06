def fibonacci():
    n = int(input("Enter no. of terms : "))
    pre = 0
    cur = 1
    for i in range(1,n+1):
        print cur
        nxt = pre + cur
        pre = cur
        cur = nxt

fibonacci()
