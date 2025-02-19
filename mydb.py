import mysql.connector

dateBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= '0615',

)

cursorObject = dateBase.cursor()

cursorObject.execute('CREATE DATABASE elderco')

print('ALL DONE')