str = "Global Warming"

print str[-4:]

print str[4:9]

if str.isalpha() == True:
    print "It has alphanumeric characters"
else:
    print "It does not have alphanumeric characters"

print str.strip("ming")
print str.strip("Glob")

print str.index('Wa')

print str.swapcase()

if str.istitle() == True:
    print "It is in Title Case"
else:
    print "It is not in Title case"

print str.replace('a','*')
