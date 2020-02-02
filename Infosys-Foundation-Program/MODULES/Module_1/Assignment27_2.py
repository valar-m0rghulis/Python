
# Fibinacci using function.

def fib_series(n):
    n1 = 0
    n2 = 1
    print(n1,n2,end=" ")
    for i in range(n):
        n3 = n2
        n2 = n1 + n2
        n1 = n3
        print(n2,end=" ")

n = int(input("Enter n:"))
fib_series(n)

'''
OUTPUT :

Enter n:6
0 1 1 2 3 5 8 13

'''
