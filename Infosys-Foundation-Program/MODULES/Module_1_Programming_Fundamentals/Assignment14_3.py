
# Program to check whether number is prime or not.

num = int(input("Enter Number : "))

if(num > 1):
    if(num == 2):
        print("Number is Prime")
    else:
        for i in range(2,num):
            if(num % i == 0):
                print("Number is not prime")
                break
            else:
                print("Number is prime")
                break;

'''
OUTPUT :

Enter Number : 17
Number is prime

'''

