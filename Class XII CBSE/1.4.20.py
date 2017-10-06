class employee(object):
    Eno = "NULL"
    Ename = "NULL"
    def Getdata(self):
        self.Eno = raw_input("Enter Employee Number : ")
        self.Ename = raw_input("Enter Employee Name : ")
    def Printdata(self):
        print "Employee Number : ",self.Eno
        print "Employee Name : ",self.Ename

class Teaching(employee):
    Dname = "NULL"
    def Inputdata(self):
        self.Getdata()
        self.Dname = raw_input("Enter Department Name : ")
    def Outdata(self):
        self.Printdata()
        print "Department Name :", self.Dname

class Non_teaching(employee):
    Designation = "NULL"
    def Inputdata(self):
        self.Getdata()
        self.Designation = raw_input("Enter Designation : ")
    def Outdata(self):
        self.Printdata()
        print "Designation : ",self.Designation

obj1 = Teaching()
obj2 = Non_teaching()

obj1.Inputdata()
obj1.Outdata()
obj2.Inputdata()
obj2.Outdata()

