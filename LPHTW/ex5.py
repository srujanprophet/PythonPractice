name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
heightcm = height * 2.54
weightkg = weight / 2.2046

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes , hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky , try to get it exactly right
print "If I add %d , %d and %d I get %d." % (
		age, height, weight, age + height + weight )
print "His weight is %d in kilos." % weightkg
print "His height is %d in centimetres" % heightcm