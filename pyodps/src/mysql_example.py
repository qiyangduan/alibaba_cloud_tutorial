# https://stackoverflow.com/questions/5687718/how-can-i-insert-data-into-a-mysql-database
import os
mysql_host = os.environ['MYSQL_HOST']
mysql_user = os.environ['MYSQL_USER']
mysql_passwd = os.environ['MYSQL_PASS']
mysql_db  = os.environ['MYSQL_DB']
print(mysql_host )
print(mysql_passwd )

import MySQLdb
conn = MySQLdb.connect(host=mysql_host,
                  user=mysql_user,
                  passwd=mysql_passwd,
                  db=mysql_db)
x = conn.cursor()

try:
   x.execute("""INSERT INTO people VALUES (%s,%s)""",("qiyangduan_age",42))
   conn.commit()
except:
   conn.rollback()

conn.close()
