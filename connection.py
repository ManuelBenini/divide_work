import mysql.connector

class Dbconnector:
    
    # def __init__(self):
    #     self.connection = None
    #     self.connection = mysql.connector.connect(host='localhost' , user='root' , passwd = 'Leagueofdraven19',port='3306',database='sakila')
    
    @classmethod
    def executeQuery(cls, query):
        cls.connection = mysql.connector.connect(host='localhost' , user='root' , passwd = 'Leagueofdraven19',port='3306',database='sakila')
        
        cursor = cls.connection.cursor()
        cursor.execute(query)
            
        return cursor.fetchall()
    
    @classmethod
    def close(cls):
        if cls.connection != None:
            cls.connection.close();