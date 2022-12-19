import mysql.connector
import json

class Dbconnector:
    
    # def __init__(self):
    #     self.connection = None
    #     self.connection = mysql.connector.connect(host='localhost' , user='root' , passwd = 'Leagueofdraven19',port='3306',database='sakila')
    
    @classmethod
    def executeQuery(cls, query):
        
        connection_data = Dbconnector.readFromFile()
        
        cls.connection = mysql.connector.connect(host=connection_data[0], user=connection_data[1], passwd=connection_data[2], port=connection_data[3], database=connection_data[4])
        
        cursor = cls.connection.cursor()
        cursor.execute(query)
            
        return cursor.fetchall()
    
    @classmethod
    def close(cls):
        if cls.connection != None:
            cls.connection.close()
            
    @classmethod
    def readFromFile(cls):
        f = open('connection.json')

        data = json.load(f)

        host = ''
        user = ''
        passwd = ''
        port = ''
        database = ''

        for i in data:
            match i:
                case 'host':
                    host = data[i]
                case 'user':
                    user = data[i]
                case 'passwd':
                    passwd = data[i]
                case 'port':
                    port = data[i]
                case 'database':
                    database = data[i]
                
        connection_data = [host, user, passwd, port, database]
        return connection_data