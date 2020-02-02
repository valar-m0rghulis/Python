

import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

# 1)

query = """SELECT username,usertype FROM users WHERE userid = 4"""
cur.execute(query)
print(cur.fetchall())

# BEFORE :
# OUTPUT :
# [('careers@amazon.com', 'Employer')]

u_name = 'lookingforjob@yahoo.com'
u_type = 'Jobseeker'

query = """UPDATE users SET username = :1, usertype = :2 WHERE userid = 4"""
cur.execute(query,(u_name,u_type))
con.commit()
query = """SELECT username,usertype FROM users WHERE userid = 4"""
cur.execute(query)
print(cur.fetchall())

# AFTER :
# OUTPUT :
# [('lookingforjob@yahoo.com', 'Jobseeker')]

# 2)

query = """SELECT password FROM users WHERE userid = 1"""
cur.execute(query)
print(cur.fetchall())

# BEFORE :
# OUTPUT :
# [('jobs@infosys',)]

pwd = input("Enter new Password : ")
query = """UPDATE users SET password = :1 WHERE userid = 1"""
cur.execute(query,{'1':pwd})
con.commit()
query = """SELECT password FROM users WHERE userid = 1"""
cur.execute(query)
print(cur.fetchall())

# AFTER :
# OUTPUT :
# Enter new Password : infosys
# [('infosys',)]

con.close()
