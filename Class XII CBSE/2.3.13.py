file2 = open("file2.txt","r+")
file1 = open("file1.txt","r+")
while True:
    Str = raw_input("Enter Content into file : ")
    file1.write(Str)
    ans = raw_input("Do you want to continue ? Y/n :")
    if ans == "n":
         break
for line in file1:
    x = line.split()
    for i in range(len(x)):
        x[i] = x[i].capitalize()
        file2.write(x[i]+" ")

file2.seek(0)
print file2.read()

file1.close()
file2.close()


