

import cx_Oracle


# 3)Invalid Username

#con = cx_Oracle.connect('infosysdb/admin@localhost/xe')

#OUTPUT :

#cx_Oracle.DatabaseError: ORA-01017: invalid username/password; logon denied



con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

# 1) Invalid Column Name

#cur.execute("DELETE FROM users WHERE user_id = 2")
#con.commit()
# OUTPUT :
# cx_Oracle.DatabaseError: ORA-00904: "USER_ID": invalid identifier

# 2) Exception Handeling

try:
    cur.execute("DELETE FROM users WHERE user_id = 2")
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("Error Details :: ",e)
finally:  
    print("Done.")
    
# OUTPUT :
# Error Details ::  ORA-00904: "USER_ID": invalid identifier
# Done. 

# 4) Wrong Table Name
   
cur.execute("DELETE FROM user WHERE userid = 2")
con.commit()

# OUTPUT :
# cx_Oracle.DatabaseError: ORA-00903: invalid table name

con.close()