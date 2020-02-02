# Python program to print string of capital letters in given strings. 

s1 = input("Enter string1 : ")
s2 = input("Enter string2 : ")
s = ""
for c in s1 +
s2:
    if(c.isupper()):
         s = s + c     
print("Resultant Stirng : ",s)


'''
OUTPUT :

Enter string1 : Hi, How are You 
Enter string2 : I am Fine how Are yoU
Resultant Stirng :  HHYIFAU

'''
