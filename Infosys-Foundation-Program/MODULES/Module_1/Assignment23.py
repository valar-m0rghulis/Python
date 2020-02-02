
#Python program to print customer details.

customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
print("CUSTOMER DETAILS")
for i in customer_details:
    print(i,customer_details[i])
print("Number of Customers:",len(customer_details))
print("Customer names in ascending order:")
for i in sorted(customer_details.values()):
    print(i,end=" ")
print("")
del customer_details[1005]
print(customer_details)
customer_details[1003] = "Mary"
print(customer_details)
if 1002 in customer_details:
    print("User id 1002 exists")
else:
    print("User id 1002 doesnt exist")


'''
OUTPUT :

CUSTOMER DETAILS
1001 John
1004 Jill
1005 Joe
1003 Jack
Number of Customers: 4
Customer names in ascending order:
Jack Jill Joe John 
{1001: 'John', 1004: 'Jill', 1003: 'Jack'}
{1001: 'John', 1004: 'Jill', 1003: 'Mary'}
User id 1002 doesnt exist

'''
