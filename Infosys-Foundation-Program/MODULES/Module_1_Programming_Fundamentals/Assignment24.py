
#Python program to print student details.

marks = {"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
print("Student Details:")
m = []
for i in marks:
    print(i,marks[i])
    m.append(marks[i])
m = sorted(m,reverse=True)
k = list(marks.keys())[list(marks.values()).index(m[0])]
k1 = list(marks.keys())[list(marks.values()).index(m[1])]
print("Student with top marks:",k,k1)
avg = sum(m)/len(m)
print("Average Marks of the class:",avg)



'''
OUTPUT :

Student Details:
John 86.5
Jack 91.2
Jill 84.5
Harry 72.1
Joe 80.5
Student with top marks: Jack John
Average Marks of the class: 82.96

'''
