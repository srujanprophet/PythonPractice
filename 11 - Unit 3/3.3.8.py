def exponent():
    base = int(input("Enter base : "))
    exp =  int(input("Enter exponent : "))
    ans = base
    for i in range(1,exp):
        ans *= base

    print "Required answer is ",ans

exponent()

