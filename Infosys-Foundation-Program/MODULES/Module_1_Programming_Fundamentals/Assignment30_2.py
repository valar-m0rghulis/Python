
# Reverse string using recurssion.

def str_rev(i):
    print(str[i],end='')
    if(i > 0):
        str_rev(i-1)
str = input("Enter a string:")
print("Original String:",str)
print("Reverse String:",end=" ")
str_rev(len(str)-1)


'''
OUTPUT :

Enter a string:Hello
Original String: Hello
Reverse String: olleH

'''
