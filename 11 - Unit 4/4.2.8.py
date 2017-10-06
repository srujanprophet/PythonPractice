studs = ["Aditya","Ankita","Naeem","Vaibhav","Omkar"]
new_studs = []
for i in range(0,len(studs)):
    print studs[i]
    char = raw_input("Do you want to keep this name? (y/n) ")
    if char == 'y':
        new_studs.append(studs[i])

print new_studs

