def fibo(n):
        if n == 0:
                return 0;
        if n == 1:
                return 1
        return fibo(n-1) + fibo(n-2)

x = int(raw_input("Enter No. of terms of fibonacci series : "))
for i in range(1,x+1):
        print fibo(i),
