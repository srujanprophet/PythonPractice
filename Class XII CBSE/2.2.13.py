class stack:
    s=[]
    def pop():
        if len(stack) <= 0:
            print 'Stack Underflow!'
            return 0
        else:
            return stack.pop()

    def display(self):
        l=len(stack.s)
        for i in range(l-1,-1,-1):
            print stack.s[i]



