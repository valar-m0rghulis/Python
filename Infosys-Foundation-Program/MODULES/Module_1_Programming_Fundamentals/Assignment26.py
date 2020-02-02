


java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}
print("Number of students enrolled for python:",len(python_course))
print("Number of students enrolled for Java:",len(java_course))
print("Number of students enrolled for both Java and Python:",len(java_course & python_course))
print("Number of students enrolled for either Java and Python but not both:",len(java_course ^ python_course))
print("Number of students enrolled for either Java or Python:",len(java_course | python_course))


'''
OUTPUT :

Number of students enrolled for python: 4
Number of students enrolled for Java: 4
Number of students enrolled for both Java and Python: 2
Number of students enrolled for either Java and Python but not both: 4
Number of students enrolled for either Java or Python: 6

'''

