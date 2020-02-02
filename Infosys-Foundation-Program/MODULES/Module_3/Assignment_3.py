

import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

cur.execute("DROP TABLE users")

# 1)

query = """CREATE TABLE users (
        userid NUMBER(10) NOT NULL PRIMARY KEY,
        username VARCHAR2(30) NOT NULL,
        password VARCHAR2(20) NOT NULL,
        usertype VARCHAR2(20) CHECK (usertype IN('Employer','Jobseeker')))"""
        
cur.execute(query)


# 2)
# 2.a)

query = """INSERT INTO users (userid, username, password, usertype)
        VALUES
        (1,'jobs@infosys.com','jobs@infosys','Employer')"""

cur.execute(query)

# 2.b)
        
u_id = 2
u_name = 'careers@accenture'
pwd = 'Acc1'
u_type = 'Employer'

query = """INSERT INTO users VALUES (:p1,:p2,:p3,:p4)"""
cur.execute(query,(u_id,u_name,pwd,u_type))

# 2.c)

u_id = 3
u_name = 'rahulitsme@gmaill.com'
pwd = 'rahulindia93'
u_type = 'Jobseeker'

query = """INSERT INTO users VALUES (:1,:2,:3,:4)"""
cur.execute(query,{'1':u_id,'2':u_name,'3':pwd,'4':u_type})

# 2.d)

u_id = int(input("Enter User ID : "))
u_name = input("Enter Username : ")
pwd = input("Enter Password : ")
u_type = input("Enter Usertype : ")

query = """INSERT INTO users VALUES (:1,:2,:3,:4)"""
cur.execute(query,{'1':u_id,'2':u_name,'3':pwd,'4':u_type})

con.commit()

# 2.e)

cur.execute("SELECT * FROM users")
print("USERS TABLE : ")
for row in cur:
    print(row)

con.close()



# OUTPUT :

'''
Enter User ID : 4
Enter Username : careers@amazon.com
Enter Password : amazonindia
Enter Usertype : Employer


USERS TABLE :
 
(1, 'jobs@infosys.com', 'jobs@infosys', 'Employer')
(2, 'careers@accenture', 'Acc1', 'Employer')
(3, 'rahulitsme@gmaill.com', 'rahulindia93', 'Jobseeker')
(4, 'careers@amazon.com', 'amazonindia', 'Employer')

'''







