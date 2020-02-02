#Pallindrom using recursion.

def ispal(str):
    if(len(str) == 1):
        return 1
    if(str[0] == str[len(str)-1]):
        return ispal((str[1:len(str)-1]))
    else:
        return 0
    
str = input("Enter a string:")
if(ispal(str)):
    print("String is a Palindrome")
else:
    print("String is not a Palindrome")

'''
OUTPUT :

Enter a string:pop
String is a Palindrome

'''
