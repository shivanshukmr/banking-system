# connects to database and gives cursor, connection objects

import mysql.connector

with open("pass.txt", "r") as f:
    output = f.readlines()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=output[0].strip("\n"),
    port=output[1],
    database="bank"
)
