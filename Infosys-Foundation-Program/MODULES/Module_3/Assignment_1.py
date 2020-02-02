'''
Write a Python program for the following:

1)Connect to Oracle database 
2)Fetch all the rows from the table Employer 
3)Display all the rows
4)Display the count of rows fetched
5)Display the description of all columns of the table 
6)Close the connection

'''


import cx_Oracle

# 1) Connect to Oracle Database
con = cx_Oracle.connect('infosys/admin@localhost/xe')

# 2) Fetch all rows
cur = con.cursor()

cur.execute("SELECT * FROM Employer")

# 3) Display all rows

print("EMPLOYER:")
for row in cur:
    print(row)

# 4) Rowcount   
print("TOTAL ROWS : ",cur.rowcount)

# 5)Description
print("DESCRIPTION :",cur.description)

# 6)Close Connection
con.close()

'''
OUTPUT:

EMPLOYER:
('C1000', 'Infosys Limited', 'jobs@infosys.com', 7896579875, 'Chennai', 'IT', 'Accounting', 'Yearly', datetime.datetime(2016, 7, 1, 0, 0), datetime.datetime(2017, 6, 30, 0, 0), 'Active')
('C1001', 'Accenture', 'careers@accenture.com', 9878776567, 'Bangalore', 'IT', 'Marketing', 'Monthly', datetime.datetime(2016, 6, 2, 0, 0), datetime.datetime(2017, 7, 1, 0, 0), 'Active')
('C1002', 'HP', 'openings@hp.com', 8789878750, 'Mumbai', 'IT', 'Marketing', 'Monthly', datetime.datetime(2016, 7, 12, 0, 0), datetime.datetime(2017, 7, 11, 0, 0), 'Active')
('C1003', 'NewGen', 'jobs@newgen.com', 8877643228, 'Bangalore', 'Manufacturing', 'Marketing', 'Yearly', datetime.datetime(2016, 9, 2, 0, 0), datetime.datetime(2017, 9, 1, 0, 0), 'Expired')

TOTAL ROWS :  4

DESCRIPTION : [('COMPANYID', <class 'cx_Oracle.STRING'>, 5, 5, None, None, 0), 
            ('COMPANYNAME', <class 'cx_Oracle.STRING'>, 50, 50, None, None, 0), 
            ('EMAILID', <class 'cx_Oracle.STRING'>, 30, 30, None, None, 1), 
            ('MOBILE', <class 'cx_Oracle.NUMBER'>, 11, None, 10, 0, 1), 
            ('CITY', <class 'cx_Oracle.STRING'>, 15, 15, None, None, 1), 
            ('INDUSTRYTYPE', <class 'cx_Oracle.STRING'>, 20, 20, None, None, 1), 
            ('FUNCTIONALAREA', <class 'cx_Oracle.STRING'>, 20, 20, None, None, 1), 
            ('MEMBERSHIPPLAN', <class 'cx_Oracle.STRING'>, 20, 20, None, None, 1), 
            ('DATEOFSIGNUP', <class 'cx_Oracle.DATETIME'>, 23, None, None, None, 1), 
            ('DATEOFRENEWAL', <class 'cx_Oracle.DATETIME'>, 23, None, None, None, 1), 
            ('RENEWALSTATUS', <class 'cx_Oracle.STRING'>, 10, 10, None, None, 1)]
'''