
courses = ("Python Programming", "RDBMS", "Web Technology", "Software Engg.")
electives = ("Business Intelligence", "Big Data Analytics")

print("Number of courses opted by John: ",len(courses))
print("Courses opted by John:",', '.join(courses))
courses = courses + electives
print("Updated Course List:",', '.join(courses))

'''
OUTPUT :

Number of courses opted by John:  4
Courses opted by John: Python Programming, RDBMS, Web Technology, Software Engg.
Updated Course List: Python Programming, RDBMS, Web Technology, Software Engg., Business Intelligence, Big Data Analytics

'''
