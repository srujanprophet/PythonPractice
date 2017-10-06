def getgrades():
	marks = []
	n = int(raw_input("Enter number of marks to be entered : "))
	print "Enter the Marks : "
	for grade in range(0,n):
		grade = int(raw_input("> "))
		marks.append(grade)	
	return marks

grades = getgrades()

def print_grades(grades):
    for grade in grades:
        print grade
 
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    var = variance / float(len(scores))
    return var
   
def grades_std_deviation(variance):
    return variance ** 0.5

def show():
	print "Grades: \n", print_grades(grades)
	print "Sum of grades: ", grades_sum(grades)
	print "Average grade: ", grades_average(grades)
	variance = grades_variance(grades)
	print "Variance: ", variance
	sd = grades_std_deviation(variance)
	print "Standard Deviation: ", sd

show()




