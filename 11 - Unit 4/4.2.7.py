studs = ["Aditya","Ankita","Naeem","Vaibhav","Omkar"]
print studs
add = raw_input("Enter one name : ")
studs.append(add)
print studs
x = int(raw_input("Enter a number : "))
if x <= len(studs):
    print studs[x-1]
else:
    print "Number provided is more than last index value"
studs.insert(0,"Kamal")
studs.insert(1,"Sanjana")
print studs
y = raw_input("Enter name : ")
for i in range(0,len(studs)):
    if y == studs[i]:
        studs.remove(studs[i])
    else:
        studs.append(y)
stud = ["Aditya","Ankita","Naeem","Vaibhav","Omkar"]
rev = stud[::-1]
print stud
print rev
studs.remove(studs[len(studs)-1])

