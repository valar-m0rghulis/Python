# Python program to diaply fibonacci series using list.

n = int(input("Enter number : "))

n1 = 0
n2 = 1
fib =[]
fib.append(n1)
fib.append(n2)
i = 0
Sum = 0
while i < n:
    Sum = n1 + n2
    fib.append(Sum)
    n1 = n2
    n2 = Sum
    i += 1
print(fib)

'''
OUTOUT :

Enter number : 5
[0, 1, 1, 2, 3, 5, 8]

'''
