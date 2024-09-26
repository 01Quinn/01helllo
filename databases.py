import mysql.connector
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'airports',
    user = 'root',
    password = 'wq453489931.',
    autocommit = True
)
print("connection")


