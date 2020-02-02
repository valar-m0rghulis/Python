
#Python Program to find Bill Amount after discount and Validate Bill Amount

bill_amount = int(input("Enter Bill Amount:"))
customer_id = int(input("Enter User ID:"))
if(customer_id in range(100,1001)):
    if(bill_amount >= 1000):
        bill_amount_discounted = bill_amount - (bill_amount * (5/100))
    elif(bill_amount >= 500 and bill_amount < 1000):
        bill_amount_discounted = bill_amount - (bill_amount * (2/100))
    elif(bill_amount > 0 and bill_amount < 500):
        bill_amount_discounted = bill_amount - (bill_amount * (1/100))
    print("Customer ID:",customer_id)
    print("Bill Amount After discount:",bill_amount_discounted)
else:
    print("Customer ID invalid")

'''
OUTPUT :

Enter Bill Amount:600
Enter User ID:101
Customer ID: 101
Bill Amount After discount: 588.0

'''
