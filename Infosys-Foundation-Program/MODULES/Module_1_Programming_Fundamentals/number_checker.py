def is_prime(num):
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

def is_even(num):
    if(num % 2 == 0):
        return True
    else:
        return False
