import mysql.connector
db_name = 'python_test_db'
mydbconnection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd='123456',
    database=db_name
)

mycursor = mydbconnection.cursor()

sqlquery ="""
            UPDATE Student
            SET Name ='Sufi'
            WHERE Name = 'Md Ala Uddin'
           """
mycursor.execute(sqlquery)
mydbconnection.commit()
print('UPDATE table Successfull')