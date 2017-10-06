def hotel_cost(nights):
    return 140 * nights
     
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    elif city == "Mumbai":
	return 600	
        
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
         cost -= 50
    elif days >= 3:
         cost -= 20
    return cost
     
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print '-' * 10, "HOLIDAY TRIP", '-' * 10
print "\nSELECT YOUR CITY\n"
print "\n1. Charlotte\n2. Tampa\n3. Pittsburgh\n4. Los Angeles\n5. Mumbai\n" 
a = raw_input("> ")
print "\n Enter no. of days\n"
b = float(raw_input("> "))
print "\n Enter extra money spent \n"
c = float(raw_input("> "))

print "\n Total Cost of the trip is: ", trip_cost(a, b, c)

