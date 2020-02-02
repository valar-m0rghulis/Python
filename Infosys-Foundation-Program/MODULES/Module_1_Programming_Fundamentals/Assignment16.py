
# Python program to check whether string is pallindrom or not.

string = input("Enter String : ")
print("Original String :",string)

reverse = string[::-1]
print("Reversed String :",reverse)

if string.lower() == reverse.lower():
    print("String is Pallindrom")
else:
    print("String is not Pallindrom")


'''
OUTPUT :

Enter String : Pop
Original String : Pop
Reversed String : poP
String is Pallindrom

'''
                     
