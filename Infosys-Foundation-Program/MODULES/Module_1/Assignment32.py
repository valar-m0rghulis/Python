

with open('courses.txt','r') as inFile:
    content = inFile.readlines()
print("File Content : ")
dictionary = dict()
array =list()

i = 0
for line in content:
    line=line.strip()
    print(line)
    dictionary[i] = line
    array.append(line)
    i += 1

print("Dictionary :",end=' ')
print(dictionary)
print("List : ",end=' ')
print(array)


'''
OUTPUT :

File Content : 
Java
Python
Javascript
PHP
Dictionary : {0: 'Java', 1: 'Python', 2: 'Javascript', 3: 'PHP'}
List :  ['Java', 'Python', 'Javascript', 'PHP']

'''
