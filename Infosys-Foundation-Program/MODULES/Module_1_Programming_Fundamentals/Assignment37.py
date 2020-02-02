
# Python program for sum of natural numbers.

def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

try:
    x = int(input("Enter n:"))
    print(sum_of_natural_numbers(x))
except ValueError:
    print("You should enter a Natural Number")

'''
OUTPUT :

Enter n:6
21

Enter n: d
You should enter a Natural Number

'''
