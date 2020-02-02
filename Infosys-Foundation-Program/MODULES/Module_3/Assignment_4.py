

import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

cur.execute("DROP TABLE vehicle")

# 1)

query = """CREATE TABLE vehicle (
        vehicleid NUMBER(5) NOT NULL PRIMARY KEY,
        vehiclename VARCHAR2(10))"""
        
cur.execute(query)

# 2)

v_id = 2001

query = """INSERT INTO vehicle VALUES (:1,:2)"""
cur.executemany(query,[(v_id,'Toyota'),(v_id + 1,'Maruti'),(v_id + 2,'Nissan'),(v_id + 3,'Hyundai')]) 

# 3)

v_id = 2005

query = """INSERT INTO vehicle VALUES (:p1,:p2)"""
cur.executemany(query,[{'p1':v_id,'p2':'Honda'},{'p1':v_id + 1,'p2':'Volkswagen'}])

con.commit()

# 4)

cur.execute("SELECT * FROM vehicle")
print("VEHICLE TABLE : ")
for row in cur:
    print(row)

con.close()




# OUTPUT:
'''
VEHICLE TABLE :
 
(2001, 'Toyota')
(2002, 'Maruti')
(2003, 'Nissan')
(2004, 'Hyundai')
(2006, 'Honda')
(2007, 'Volkswagen')

'''