from datetime import datetime
class Train(object):
    Tno = "NULL"
    Tname = "NULL"
    StartStation = "NULL"
    Destination = "NULL"
    Departure = "NULL"
    Arrival = "NULL"
    def getdata(self):
        self.Tno = raw_input("Enter Train Number :")
        self.Tname = raw_input("Enter Train Name :")
        self.StartStation = raw_input("Enter Starting Station :")
        self.Destination = raw_input("Enter Destination :")
        self.Departure = datetime.strptime(raw_input("Enter Departure Time :"),'%H%M%S')
        self.Arrival = datetime.strptime(raw_input("Enter Time of Arrival :"),'%H%M%S')
    def putdata(self):
        print "Train Number : ",self.Tno,'\n',"Train Name : ",self.Tname,'\n',"Starting Station : ",\
            self.StartStation,'\n',"Destination : ",self.Destination
        print "Time of Departure : ",self.Departure,'\n',"Time of Arrival : ",self.Arrival
    def search(self):
        x = raw_input("Enter Train Number : ")

class passenger(Train):
    TicketNo = "NULL"
    PNR = "NULL"
    Pname = "NULL"
    Gender = "NULL"
    Age = "NULL"
    Address = "NULL"
    Phone = "NULL"
    def getdata1(self):
        self.search()
        self.TicketNo = raw_input("Enter Ticket Number : ")
        self.PNR = raw_input("Enter PNR : ")
        self.Pname = raw_input("Enter Name :")
        self.Gender = raw_input("Enter Gender:")
        self.Age = raw_input("Enter Age:")
        self.Address = raw_input("Enter Address :")
        self.Phone = raw_input("Enter Phone No. :")
    def display(self):
        self.putdata()
        print "Ticket Number :",self.TicketNo
        print "PNR :",self.PNR
        print "Passenger Name :",self.Pname
        print "Gender :",self.Gender
        print "Age :",self.Age
        print "Address :",self.Address
        print "Phone Number : ",self.Phone


obj = passenger()
Trains = int(raw_input("Enter no. of Trains :"))
for j in range(Trains):
    obj.getdata()
Passengers = int(raw_input("Enter no. of Passengers :"))
for i in range(Passengers):
    obj.getdata1()
    obj.display()




