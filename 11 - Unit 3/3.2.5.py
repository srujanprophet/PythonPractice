def odd(x):
    if x % 2 == 0:
        return False
    else:
        return True

a = int(raw_input("Enter a number : "))
print odd(a)
