

import math

def course_comb(crs):
    combinations = math.factorial(crs)
    return combinations

courses = int(input("Enter number of Cources avialable : "))

print("Total number of Course combinations : ", course_comb(courses))


'''
OUTPUT :

Enter number of Cources avialable : 6
Total number of Course combinations :  720

'''
