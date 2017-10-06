class accomodation(object):
    RoomNumber = raw_input("Enter Room Number :")
    RoomType = raw_input("Enter Room Type :")
    Rent = int(raw_input("Enter Rent :"))

class meals(object):
    MealCode = raw_input("Enter Meal Code :")
    MealName = raw_input("Enter Meal Name :")
    Price = int(raw_input("Enter Meal Price :"))

class customer(accomodation,meals):
    CNo = raw_input("Enter Customer No. :")
    CName = raw_input("Enter Customer Name :")
    Address = raw_input("Enter Customer Address :")



