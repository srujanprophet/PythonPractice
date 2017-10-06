class student(object):
    Rollnumber = "NULL"
    name = "NULL"
    def Getdata(self):
        self.Rollnumber = raw_input("Enter Roll No. : ")
        self.name = raw_input("Enter Name : ")
    def Printdata(self):
        print "Roll No. : ",self.Rollnumber
        print "Name : ", self.name

class marks(student):
    marks = []
    def Inputdata(self):
        for i in range(5):
            print "Enter marks in subject",i+1
            x = raw_input()
            self.marks.append(x)
    def Outdata(self):
        self.Printdata()
        print "Marks",self.marks

obj = marks()
obj.Getdata()
obj.Inputdata()
obj.Outdata()

