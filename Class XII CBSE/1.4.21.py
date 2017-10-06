class employee(object):
    Eno = "NULL"
    Ename = "NULL"
    def Getdata(self):
        self.Eno = raw_input("Enter Employee No. : ")
        self.Ename = raw_input("Enter Employee Name : ")
    def Printdata(self):
        print "Employee Number:",self.Eno,'\n',"Employee Name",self.Ename

class payroll(employee):
    Salary = "NULL"
    def Inputdata(self):
        self.Getdata()
        self.Salary = int(raw_input("Enter Salary : "))
    def Outdata(self):
        self.Printdata()
        print "Salary : ",self.Salary

class leave(payroll):
    Noofdays = 0
    def acceptdata(self):
        self.Inputdata()
        self.Noofdays = raw_input("Enter no. of days : ")
    def showdata(self):
        self.Outdata()
        print "No. of days taken leave:",self.Noofdays

obj1 = leave()
obj1.acceptdata()
obj1.showdata()
