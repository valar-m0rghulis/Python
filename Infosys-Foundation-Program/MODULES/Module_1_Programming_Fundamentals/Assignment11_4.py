
'''
The ﬁnance department of a company wants to compute the monthly pay of its employees.
Monthly pay shouldbe calculated as mentioned in the formula below.
Display all the employee details.
Monthly Pay = Number of hours worked in a week * Pay rate per hour * No. of weeks in a month
•The number of hours worked by the employee in a week should be considered as 40
•Pay rate per hour should be considered as Rs.400
•Number of weeks in a month should be considered as 4
Write a Python program to implement the above real world problem.
'''

emp_name = input("Enter employee name : ")
number_of_hours = 40
rate_per_hour = 400
number_of_weeks = 4

monthly_pay = number_of_hours * rate_per_hour * number_of_weeks

print("-------[ Employee Details ]---------")

print("Employee Name          : ", emp_name)
print("Number of Hours Worked : ", number_of_hours)
print("Pay rate per hour      : ", rate_per_hour)
print("Number of Weeks        : ", number_of_weeks)

print("Monthly Pay  : ", monthly_pay)

'''
OUTPUT :

Enter employee name : Jhon
-------[ Employee Details ]---------
Employee Name          :  Jhon
Number of Hours Worked :  40
Pay rate per hour      :  400
Number of Weeks        :  4
Monthly Pay  :  64000

'''
