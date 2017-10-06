class Furniture(object):
    Type = "NULL"
    Model = "NULL"
    def getType(self):
        return self.Type
    def getModel(self):
        return self.Model
    def show(self):
        print self.Type,' ',self.Model

class sofa(Furniture):
    No_of_seats = 0
    Cost = 0
    def getSeats(self):
        return self.No_of_seats
    def getCost(self):
        return self.Cost
    def show(self):
        print self.No_of_seats,' ',self.Cost

obj1 = sofa()
print obj1.Model
