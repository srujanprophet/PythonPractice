class employee(object):
    Eno = "NULL"
    Ename = "NULL"
    Designation = "NULL"
    Address = "NULL"
    PhoneNo = "NULL"
    def getdata(self):
        self.Eno = raw_input("Enter Employee No. : ")
        self.Ename = raw_input("Enter Employee Name : ")
        self.Designation = raw_input("Enter Designation : ")
        self.Address = raw_input("Enter Address : ")
        self.PhoneNo = raw_input("Enter Phone No. : ")
    def putdata(self):
        print "Employee No. : ",self.Eno
        print "Employee Name : ",self.Ename
        print "Designation : ",self.Designation
        print "Address : ",self.Address
        print "Phone No. :",self.PhoneNo

class salary(employee):
    Basicpay = 0
    DA = 0
    HRA = 0
    Grosspay = 0
    PF = 0
    IncomeTax = 0
    Netpay = 0
    def getdata1(self):
        self.getdata()
        self.Basicpay = int(raw_input("Enter Basic Pay : "))
    def calculate(self):
        self.Netpay = self.Basicpay
    def display(self):
        self.putdata()
        print "Basic Pay : ",self.Basicpay,'\n',"DA : ",self.DA,'\n',"HRA : ",self.HRA,'\n',"Gross Pay : ",self.Grosspay
        print "PF : ",self.PF,'\n',"Income Tax : ",self.IncomeTax,'\n',"Net Pay : ",self.Netpay

n = int(raw_input("Enter no. of Employees : "))
for i in range(n):
    print "Employee ",i+1
    obj = salary()
    obj.getdata1()
    obj.calculate()
    obj.display()
