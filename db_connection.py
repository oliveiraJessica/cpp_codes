import mysql.connector

cnx = mysql.connector.connect(user='root', host='localhost', port='3307', db='cadastro')
cursor = cnx.cursor()


class MySQLConnection():
    def __init__(self):
        try:
           sql = "select * from users"
           cursor.execute(sql)
           results = cursor.fetchall()
           for row in results:
               print(row)
        finally:
           # cnx.close()
            print('What is this finally for?')

    def execute_query(self, query):
        try:
            cursor.execute(query);
            return cursor.fetchone()
        except Exception as e:
            print('Somethng wrong with query')
            print(e)
        finally:
            print('What is this finally for?')
