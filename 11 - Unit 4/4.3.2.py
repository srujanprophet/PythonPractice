hod = dict()
n = int(raw_input("Enter no. of subjects : "))
for i in range(0,n):
    a = raw_input("Enter Subject : ")
    b = raw_input("Enter head of the department : ")
    hod[a] = b

print "Subject",'             ',"HOD"
l = hod.keys()
for i in l:
    print i,'              ',hod[i]
