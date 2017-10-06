class ITEMINFO:
    ICode = 0
    Item = "NULL"
    Price = 0
    Qty = 0
    Discount = 0
    Netprice = 0

    def FindDisc(self):
        if self.Qty <= 10:
            self.Discount = 0
        elif self.Qty >= 20:
            self.Discount = 20
        else:
            self.Discount = 15

    def __init__(self):
        print "---------- Welcome to ChevronStores ----------"

    def Buy(self):
        self.ICode = raw_input("Enter Item Code : ")
        self.Item = raw_input("Enter Item : ")
        self.Price = int(raw_input("Enter Price : "))
        self.Qty = int(raw_input("Enter Quantity : "))
        self.FindDisc()
        self.Netprice = self.Price*self.Qty - self.Discount

    def ShowAll(self):
        print "Item Code : \t",self.ICode
        print "Item : \t",self.Item
        print "Price : \t",self.Price
        print "Quantity : \t",self.Qty
        print "Discount : \t", self.Discount
        print "Net Price : \t",self.Netprice

obj = ITEMINFO()
obj.Buy()
obj.ShowAll()
