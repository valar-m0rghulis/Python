
import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

print("Before Update :")
cur.execute("SELECT * FROM vehicle")
print("VEHICLE TABLE : ")
for row in cur:
    print(row)
    
n = cur.rowcount
query = """UPDATE vehicle SET vehicleid = :1 WHERE vehicleid = :2"""

for i in range(1,n+1):
    cur.execute(query,{'1':int('100'+str(i)),'2':int('200'+str(i))})

query = """UPDATE vehicle SET vehiclename = 'Mahindra' WHERE vehicleid = 1003"""
cur.execute(query)
con.commit()

print("After Update :")
cur.execute("SELECT * FROM vehicle")
print("VEHICLE TABLE : ")
for row in cur:
    print(row)
    
con.close()

# OUTPUT :
'''
Before Update :

VEHICLE TABLE :
 
(2001, 'Toyota')
(2002, 'Maruti')
(2003, 'Nissan')
(2004, 'Hyundai')
(2005, 'Honda')
(2006, 'Volkswagen')

After Update :

VEHICLE TABLE : 

(1001, 'Toyota')
(1002, 'Maruti')
(1003, 'Mahindra')
(1004, 'Hyundai')
(1005, 'Honda')
(1006, 'Volkswagen')

'''