
# Addition of n natural numbers using fiction.


def addition(num):
    i = 1
    Sum = 0
    while i <= num:
        Sum = Sum  + i
        i += 1
    print("Addition = ", Sum)
    
n = int(input("Enter number:"))

addition(n)


'''
OUTPUT :

Enter number:6
Addition =  21

'''
