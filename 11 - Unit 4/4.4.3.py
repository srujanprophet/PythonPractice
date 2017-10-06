T = tuple()
n = int(raw_input("Enter no. of employees : "))

for i in range(n):
    x = int(raw_input("Enter Salaries : "))
    T = T + (x,)

print "Max. Salary is ",    max(T)
print "Min. Salary is ",    min(T)
