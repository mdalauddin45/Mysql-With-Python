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
           INSERT INTO Student(Roll,Name)
           values('101','Md Ala Uddin')
           """
mycursor.execute(sqlquery)
mydbconnection.commit()
print('Insert table Successfull')