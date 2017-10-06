def factorial():
    fact = 1
    n = int(input("Enter no. whose factorial is required : "))
    for i in range(1,n+1):
        fact *= i
    print  n,"! = ", fact

factorial()
