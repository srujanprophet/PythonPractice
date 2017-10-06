from pickle import dump,load

numerals = dict()
numerals['M'] = 1000
numerals['D'] = 500
numerals['C'] = 100
numerals['L'] = 50
numerals['X'] = 10
numerals['V'] = 5
numerals['I'] = 1

with open("Roman1.txt",'wb') as ofile :
    dump(numerals,ofile)
    ofile.close()

ifile = open("Roman1.txt",'rb')
try :
    while True:
        r = []
        r = load(ifile)
        x = raw_input("Enter Roman Numeral : ")
        sum = 0
        for i in range(len(x)):
            sum = sum + r[x[i]]
        print sum
except EOFError:
    pass
ifile.close()
