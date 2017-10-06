from datetime import datetime
s1 = raw_input("Enter Time 1 :")
s2 = raw_input("Enter Time 2 : ")
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)
print tdelta
