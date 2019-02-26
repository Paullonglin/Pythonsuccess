import pymysql
db=pymysql.connect('localhost','root','66688888','testdb')
conn=db.cursor()
sql='select * from EMPLOYEE'
try:
    conn.execute(sql)
    data=conn.fetchone()
    print(data)
except:
    db.rollback()
db.close()


