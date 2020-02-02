
# Variety Retail Store.

catalog = [("Sofa Set",20000),("Dining Table",8500),("T.V. Stand",4599),("Cupboard",13920)]
name = input("Which furniture do you want : ")
quantity = int(input("what is the quantity required : "))
i = [item for item in catalog if item[0] == name]
if(i):
    if(quantity > 0):
        bill_amount = i[0][1] * quantity
        print("Bill Amount :",bill_amount)
else:
    print("Requested Furniture not available")


'''
OUTPUT :

Which furniture do you want : Cupboard
what is the quantity required : 5
Bill Amount : 69600

'''
