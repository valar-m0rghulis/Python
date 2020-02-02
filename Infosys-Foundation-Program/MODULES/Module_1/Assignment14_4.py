
# Pyhton program to print fibonacci series upto n terms.

n = int(input("Enter number : "))

n1 = 0
n2 = 1
print(n1,n2,end=" ")
i = 1
Sum = 0
while i <= n:
    Sum = n1 + n2
    print(Sum,end=" ")
    n1 = n2
    n2 = Sum
    i += 1

'''
OUTPUT :

Enter number : 8
0 1 1 2 3 5 8 13 21 34

'''

    
    


    
