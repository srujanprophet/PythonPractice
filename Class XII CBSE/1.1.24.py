str = raw_input("Enter String : ")
words = 1
for i in str:
    if i == ' ':
        words += 1

print "No. of words : ",words
