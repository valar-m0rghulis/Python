
'''
Identify the sections of the given program where the coding standards are not followed and correct them.
'''

itemNo=1005  # Binary operators should be enclosed with spaces.
unitprice = 250 # 2 words should be separated by underscore
quantity = 2
amount=quantity*unitprice # Binary operators should be enclose with spaces.
print("Item No:", itemNo)
print("Bill Amount:", amount)

# Corrected:

itemNo = 1005
unitprice = 250
quantity = 2
amount = quantity * unitprice
print("Item No:", itemNo)
print("Bill Amount:", amount)


'''
OUTPUT :

Item No: 1005
Bill Amount: 500
Item No: 1005
Bill Amount: 500

'''
