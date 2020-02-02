mylist = [1,2,3,"4",5]
sum = 0
try:
    for i in mylist:
        sum = sum + i
except TypeError:
    print("One of the values is a string and cannot be added")
print(sum)
try:
    print(mylist[5])
except IndexError:
    print("Trying to access value which does not exist")


'''
OUTPUT :

One of the values is a string and cannot be added
6
Trying to access value which does not exist

'''
