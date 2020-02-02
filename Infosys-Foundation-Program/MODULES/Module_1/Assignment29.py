# Fibonacci using recurssion

def fibo(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

x = int(input("Enter n:"))

if(x < 0):
    print("Invalid x, should be positive")
    
print(fibo(x))


'''
OUTPUT :

Enter n:6
8

'''
