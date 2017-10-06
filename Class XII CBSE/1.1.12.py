Eno = raw_input("Enter Employee Number : ")
Ename = raw_input("Enter Employee Name : ")
bpay = float(raw_input("Enter Basic Pay : "))

if bpay > 100000:
    HRA = 0.15*bpay
    DA = 0.08*bpay

elif bpay <= 50000:
    HRA = 0.05*bpay
    DA = 0.03*bpay

else:
    HRA = 0.1*bpay
    DA = 0.05*bpay

print "Employee No. ",'     ',"Employee Name ",'        ',"Basic Pay ",'        ',"HRA ",'      ',"DA "
print "-----------------------------------------------------------------------------------------------"
print Eno,'         ',Ename,'           ',bpay,'          ',HRA,'        ',DA
