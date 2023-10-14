import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='0000'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE training")  
print("Database 'training' created successfully!")
print("It All Done!")
