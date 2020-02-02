

import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

# 1) 

#cur.execute("INSERT INTO product VALUES('P106','Jams',105)")
#con.close()

# OUTPUT :
# cx_Oracle.DatabaseError: ORA-00947: not enough values

# 2) Exception Handeling

try:
    cur.execute("INSERT INTO product VALUES('P106','Jams',105)")
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("Error Details :: ",e)
finally:  
    print("Done.")
    
# OUTPUT :
# Error Details ::  ORA-00947: not enough values
# Done.


con.close()