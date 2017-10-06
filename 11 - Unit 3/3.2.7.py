def fourthPower(x):
    ans = 1
    for i in range(1,5):
        ans *= x
    return ans

t = int(raw_input("Enter a number : "))
print fourthPower(t)
