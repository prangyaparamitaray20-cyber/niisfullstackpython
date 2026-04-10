import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="niis"
)
if con:
    print("connected")
else:
    print("not connected")