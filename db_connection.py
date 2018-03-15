import mysql.connector
import singleton

def singleton(myClass):
    instances = {}
    def getInstace(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstace

@singleton
class MySQLConnection():
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', host='localhost', port='3307', db='cadastro')
        self.cursor = self.cnx.cursor()
        try:
           sql = "select * from users"
           self.cursor.execute(sql)
           results = self.cursor.fetchall()
           for row in results:
               print(row)
        finally:
           # cnx.close()
            print('What is this finally for?')

    def execute_query(self, query):
        try:
            self.cursor.execute(query);
            return self.cursor.fetchone()
        except Exception as e:
            print('Somethng wrong with query')
            print(e)
        finally:
            print('What is this finally for?')
