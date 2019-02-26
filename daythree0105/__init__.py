import pymysql

conn = pymysql.connect('localhost', 'root', '66688888', 'paul')
cursor = conn.cursor()
sql = '''create table pl(
   id INT NOT NULL AUTO_INCREMENT,
   PRIMARY KEY ( id )
);'''
cursor.execute(sql)
conn.close()
