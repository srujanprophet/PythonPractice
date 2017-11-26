import sys
target_int = raw_input("How many integers?")
try:
    target_int = int(target_int)
except ValueError:
    sys.exit("You must enter an integer")

ints = list()
count = 0
while count < target_int:
    new_int = raw_input("Please enter integer {0}:".format(count+1))
    isint = True
    try:
        new_int = int(new_int)

    except:
        print("You must enter an integer")
        isint = False
    if isint == True:
        ints.append(new_int)
        count += 1
for value in ints:
    print(str(value))
