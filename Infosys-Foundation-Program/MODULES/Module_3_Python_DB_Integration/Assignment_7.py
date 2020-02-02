

import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

print("BEFORE DELETE : ")

cur.execute("SELECT * FROM users")
print("USERS TABLE : ")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM vehicle")
print("VEHICLE TABLE : ")
for row in cur:
    print(row)


cur.execute("DELETE FROM users WHERE userid = 1")
con.commit()

v_id = int(input("Enter Vehicle ID :"))

cur.execute("DELETE FROM vehicle WHERE vehicleid = :1",{'1':v_id})
con.commit()

print("AFTER DELETE : ")

cur.execute("SELECT * FROM users")
print("USERS TABLE : ")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM vehicle")
print("VEHICLE TABLE : ")
for row in cur:
    print(row)

con.close()

# OUTPUT :
'''
BEFORE DELETE : 

USERS TABLE : 
(1, 'jobs@infosys.com', 'infosys', 'Employer')
(2, 'careers@accenture', 'Acc1', 'Employer')
(3, 'rahulitsme@gmaill.com', 'rahulindia93', 'Jobseeker')
(4, 'lookingforjob@yahoo.com', 'amazonindia', 'Jobseeker')

VEHICLE TABLE : 
(1001, 'Toyota')
(1002, 'Maruti')
(1003, 'Mahindra')
(1004, 'Hyundai')
(1005, 'Honda')
(1006, 'Volkswagen')

Enter Vehicle ID :1003

AFTER DELETE : 

USERS TABLE : 
(2, 'careers@accenture', 'Acc1', 'Employer')
(3, 'rahulitsme@gmaill.com', 'rahulindia93', 'Jobseeker')
(4, 'lookingforjob@yahoo.com', 'amazonindia', 'Jobseeker')

VEHICLE TABLE : 

(1001, 'Toyota')
(1002, 'Maruti')
(1004, 'Hyundai')
(1005, 'Honda')
(1006, 'Volkswagen')

'''