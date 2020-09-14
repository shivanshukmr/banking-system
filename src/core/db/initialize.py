import mysql.connector
import os.path


pass_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "pass.txt")

with open(pass_path, "r") as f:
    output = f.readlines()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=output[0].strip("\n")
)

cursor = db.cursor()
query = "create database if not exists bank"
cursor.execute(query)
db.commit()
