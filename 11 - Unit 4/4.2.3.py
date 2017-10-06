
def chop(l):
    l.remove(l[0])
    l.remove(l[len(l)-1])
    return None

def middle(L):
    new = L[1:len(L)-1]
    return new

n = int(raw_input("Enter length of list : "))
print "Enter elements of list -"
x = []
for i in range(0,n):
    y = int(raw_input("Enter number : "))
    x.append(y)

print middle(x)
