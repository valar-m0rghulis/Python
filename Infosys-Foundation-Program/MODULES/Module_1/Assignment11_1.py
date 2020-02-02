
# Python program to swap values without third variable.



a = 4
b = 5

print("Before Swapping :")
print("a = ", a)
print("b = ", b)

a += b

b = a - b

a = a - b

print("After Swapping :")
print("a = ", a)
print("b = ", b)


'''
OUTPUT :

Before Swapping :
a =  4
b =  5
After Swapping :
a =  5
b =  4

'''
