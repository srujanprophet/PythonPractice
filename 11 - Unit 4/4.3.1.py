city = dict()
name = raw_input("Enter City Name : ")
for i in range(5):
    a = raw_input("Enter Year : ")
    b = raw_input("Enter population : ")
    city[a] = b

print "Population of", name
l = city.keys()
for i in l:
    print i,' : ',city[i]
