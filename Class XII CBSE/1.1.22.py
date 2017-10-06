username = "admin"
password = "12345"
user = raw_input("Enter Username : ")
passs = raw_input("Enter Password : ")
if user == username and passs == password:
    print "Login Successful"
elif user == username and passs != password:
    print "Incorrect Password"
elif user != username and passs == password:
    print "Incorrect Username"
else:
    print "Login Failed!"
