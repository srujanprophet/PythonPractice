class trainer(object):
    Name = "NULL"
    T_ID = "NULL"
    def getName(self):
        print self.Name
    def getTID(self):
        print self.T_ID

class learner(object):
    L_Name = "NULL"
    L_ID = "NULL"
    def getName(self):
        print self.L_Name
    def getLID(self):
        print self.L_ID

class Institute(trainer,learner):
    I_Name = "NULL"
    I_Code = "NULL"
    def getName(self):
        print self.I_Name
    def getICode(self):
        print self.I_Code

obj = Institute()
print obj.getTID()
