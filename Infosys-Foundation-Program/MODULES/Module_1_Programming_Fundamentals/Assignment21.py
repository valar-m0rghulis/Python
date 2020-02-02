
# Variety Retail Store

furniture = ["Sofa Set","Dining Table","T.V. Stand","Cupboard"]
cost = [20000,8500,4599,13920]

order = input("Which Furniture Do you want:")

if order in furniture:
    i = furniture.index(order)
    quantity = int(input("Enter the quantity required:"))
    if(quantity < 0):
        print("Invalid Quantity")
    else:
        bill_amount = cost[i] * quantity
        print("Amount to be paid:",bill_amount)
else:
    print("Requested Furniture is not available")


'''
OUTPUT :

Which Furniture Do you want:Cupboard
Enter the quantity required:5
Amount to be paid: 69600

'''
