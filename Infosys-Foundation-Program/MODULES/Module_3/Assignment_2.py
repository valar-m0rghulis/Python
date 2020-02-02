

import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

# 1)

cur.execute("SELECT companyname,emailid FROM employer WHERE industrytype = 'IT' AND city = 'Bangalore'")

print(cur.fetchall())
    
# OUTPUT:
# [('Accenture', 'careers@accenture.com')]

# 2)

myCity = 'Bangalore'
status = 'Active'

query = "SELECT companyname,mobile,emailid FROM employer WHERE city = :c AND renewalstatus = :s"
cur.execute(query,(myCity,status))
print(cur.fetchall())

# OUTPUT:
# [('Accenture', 9878776567, 'careers@accenture.com')]


# 3)

cur.execute(query,(status,myCity))
print(cur.fetchall())


# OUTPUT:
# []

# 4)

query = "SELECT companyname,mobile,emailid FROM employer WHERE city =:a AND renewalstatus = :b"
cur.execute(query,{'a':myCity,'b':status})
print(cur.fetchall())

# OUTPUT:
# [('Accenture', 9878776567, 'careers@accenture.com')]

# 5)

cur.execute(query,{'b':status,'a':myCity})
print(cur.fetchall())

# OTPUT:
# [('Accenture', 9878776567, 'careers@accenture.com')]


con.close()