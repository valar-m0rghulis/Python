#Python Program to find Bill Amount after discount. 

bill_amount = int(input("Enter Bill Amount:"))

if(bill_amount >= 1000):
    bill_amount_discounted = bill_amount - (bill_amount * (5/100))
    
elif(bill_amount >= 500 and bill_amount < 1000):
    bill_amount_discounted = bill_amount - (bill_amount * (2/100))
    
elif(bill_amount > 0 and bill_amount < 500):
    bill_amount_discounted = bill_amount - (bill_amount * (1/100))

print("Bill Amount After discount:",bill_amount_discounted)


'''
OUTPUT :

Enter Bill Amount: 500
Bill Amount After discount: 490.0

'''
