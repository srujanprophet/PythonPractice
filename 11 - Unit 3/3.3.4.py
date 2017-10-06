def countdown():
    x = input("Enter any number : ")
    if x > 0:
        while x!= 0:
            print x
            x -= 1
        print 0
    else:
        while x!= 0:
            print x
            x += 1
        print 0

countdown()
