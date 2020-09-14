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

query = '''create table bank.users
    (firstname varchar(100) NOT NULL,
    lastname varchar(100) NOT NULL,
    accno int(6) PRIMARY KEY AUTO_INCREMENT,
    passwd varchar(32) NOT NULL,
    date_created datetime NOt NULL,
    balance int)'''

cursor.execute(query)
db.commit()

query = '''alter table bank.users auto_increment=100000'''
cursor.execute()
db.commit()

query = '''create table bank.transactionhistory
(
    user1accno int(6),
    user2accno int(6),
    amount int(),
    datetime datetime
)
