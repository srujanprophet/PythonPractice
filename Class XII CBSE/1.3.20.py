class SOCIETY:
    society_name = "NULL"
    house_no = 0
    no_of_members = 0
    flat = 0
    income = 0
    def __init__(self):
        self.society_name = "Surya Apartments"
        self.flat = "A Type"
        self.house_no = 20
        self.no_of_members = 3
        self.income = 25000

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A Type"
        elif self.income < 15000:
            self.flat = "B Type"
        else:
            self.flat = "C Type"

    def Inputdata(self):
        self.society_name = raw_input("Enter Name of Society : ")
        self.no_of_members = raw_input("Enter No. of Members : ")
        self.income = int(raw_input("Enter Income : "))
        self.allocate_flat()

    def Showdata(self):
        print "-------------------------------------------------------"
        print "Society Name : ",self.society_name
        print "House Number : ",self.house_no
        print "No. of Members : ",self.no_of_members
        print "Flat : ",self.flat
        print "Income : ",self.income

obj = SOCIETY()
obj.Inputdata()
obj.Showdata()




