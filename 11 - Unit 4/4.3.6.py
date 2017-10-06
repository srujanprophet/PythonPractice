c=dict()
n = input("Enter total number ")
i=1
while i<=n:
    a=raw_input("enter place")
    b=raw_input("enter number")
    c[a]=b
    i=i+1

print "place","\t","number"

for i in c:
    print i,"\t",c[i]
