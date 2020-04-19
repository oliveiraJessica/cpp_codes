import mysql.connector

cnx = mysql.connector.connect(user='root', host='localhost', port='3307')
cursor = cnx.cursor()
try:
   sql = "select * from cursos"
   cursor.execute("use cadastro")
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
       print(row)
finally:
    cnx.close()
