class student(object):
    studno = raw_input("Enter Student Number :")
    studname = raw_input("Enter Student Name :")

class graduate(student):
    subjectcode = raw_input("Enter Subject Code :")
    subjectname = raw_input("Enter Subject Name :")

class postgraduate(graduate):
    mastersubjectcode = raw_input("Enter Master Subject Code :")
    mastersubjectname = raw_input("Enter Master Subject Name :")
