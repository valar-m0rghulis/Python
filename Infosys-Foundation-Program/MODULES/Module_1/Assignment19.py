
# Python program to print letters at even positon.


accepted_string = input("Enter String
                        :")
print(accepted_string)

resultant_string = ""

for c in accepted_string:
    if accepted_string.index(c)% 2==0:
        if c.isalpha():
            resultant_string = resultant_string + c
            
print(resultant_string)

expected_output = resultant_string[::-1]

print(expected_output)


'''
OUTPUT :

Enter String :FdbFFKKfBdjjdlDLsl
FdbFFKKfBdjjdlDLsl
FbFFBjjDs
sDjjBFFbF

'''
