
f = open("file.txt",'r+')  # Part 1
print f.read()

j = 1                       # Part 3
for line in f:
    if j == 3:
        print i,":",line
        i += 1

print '\n'                      # Part 4
f.seek(10)
print f.readline()

k = int(raw_input("Enter Line Number : "))              # Part 5
t = 1
for line in f:
    if t == k:
        print t,":",line
    t += 1

f = open("file.txt",'a')                                            # Part 2
while True:
    x = raw_input("Enter content :")
    f.write(x)
    ans = raw_input("Do you want to continue writing (y/n) ? :")
    if ans == 'n':
        break
f = open("file.txt",'r+')
i = 1
for line in f:
    print i,":",line
    i += 1

