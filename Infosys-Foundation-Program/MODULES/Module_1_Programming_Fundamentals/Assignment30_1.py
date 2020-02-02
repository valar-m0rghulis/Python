
# n mulptiples of 3.


def multiple(n):
    
    if n > 1:
        multiple(n-1) 
    print( n * 3)
            
n = int(input("Enter number:"))
multiple(n)

'''
OUTPUT :

Enter number:6
3
6
9
12
15
18

'''


