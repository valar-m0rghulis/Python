

with open('student_details.txt','r') as inFile:
    content = inFile.readlines()

list_of_list=list()
list_of_dictionary=list()

i =0

for line in content:
    line = line.strip()
    print(line)
    item = line.split()
    list_of_list.append(item)
    d = dict()
    d[item[0]]=item[1]
    list_of_dictionary.append(d)
print(list_of_list)
print(list_of_dictionary)


'''
OUTPUT :

101 Rahul
102 Julie
103 Helena
104 Kally
[['101', 'Rahul'], ['102', 'Julie'], ['103', 'Helena'], ['104', 'Kally']]
[{'101': 'Rahul'}, {'102': 'Julie'}, {'103': 'Helena'}, {'104': 'Kally'}]

'''
