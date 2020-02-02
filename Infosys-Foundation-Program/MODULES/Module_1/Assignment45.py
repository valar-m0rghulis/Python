
import re
cust_details = "Hello John, your customer id is j181"
r = re.search("hello",cust_details,re.I)
print(r.group())
r2 = re.search(r"\D\d{3}$",cust_details)
print(r2.group())
def dig(r):
    return r.group()[1:]
cust_details = re.sub(r"j\d{3}",dig,cust_details)
cust_details = re.sub("id","ID",cust_details)
print(cust_details)


'''
OUTPUT :

Hello
j181
Hello John, your customer ID is 181

'''

