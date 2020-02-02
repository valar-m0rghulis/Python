

import cx_Oracle

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

cur.execute("DROP TABLE account")

# 1)

query = """CREATE TABLE account (
        customerid NUMBER NOT NULL PRIMARY KEY,
        accountno VARCHAR2(15),
        accounttype VARCHAR2(15) CHECK(accounttype IN('Savings','Current','Recurring')),
        balance NUMBER)"""      
cur.execute(query)
con.commit()

# 2)

uid = 100
acid = 'IBI100'

query = "INSERT INTO account VALUES(:1,:2,:3,:4)"
cur.executemany(query,
                [(uid+1,acid+'1','Savings',0),
                 (uid+2,acid+'2','Current',1200),
                 (uid+3,acid+'3','Savings',6543),
                 (uid+4,acid+'4','Recurring',7500),
                 (uid+5,acid+'5','Current',0)])
con.commit()


# 3)

query = """SELECT customerid,balance FROM account WHERE
            balance = (SELECT MAX(balance) FROM account)"""
cur.execute(query)
print(cur.fetchall())

# OUTPUT :
# [(104, 7500)]

# 4)

query = "SELECT balance FROM account WHERE customerid = 102"
cur.execute(query)
acct_bal = cur.fetchone()[0]

print("acct_bal : ",acct_bal) 

# OUTPUT :
# acct_bal :  1200


# 5)

acct_bal = acct_bal + 2000

query = "UPDATE account SET balance = :b WHERE customerid = 102"
cur.execute(query,{'b':acct_bal})
con.commit()

# 6)

query = "SELECT balance FROM account WHERE customerid = 102"
cur.execute(query)
print(cur.fetchall())

# OUTPUT :
# [(3200,)]


# 7)

query = "DELETE FROM account WHERE accounttype = 'Current' AND balance = 0"
cur.execute(query)
con.commit()

con.close()