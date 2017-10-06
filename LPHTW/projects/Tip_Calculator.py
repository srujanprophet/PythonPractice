meal = float(raw_input("Enter cost of meal > "))

tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print "Total money spent is : "
print("%.2f" % total)
