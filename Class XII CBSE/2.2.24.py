class stack:
    s=[]
    def push(self):
        a=raw_input("Enter Student Name:")
        stack.s.append(a)
    def display(self):
        l=len(stack.s)
        for i in range(l-1,-1,-1):
            print stack.s[i]

s = stack()
n = int(raw_input("Enter No. of Names : "))
for i in range(n):
    s.push()
s.display()


