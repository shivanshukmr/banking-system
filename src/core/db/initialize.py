import mysql.connector
import os.path

pass_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "pass.txt")

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

query = '''create table if not exists bank.users
    (firstname varchar(100) NOT NULL,
    lastname varchar(100) NOT NULL,
    accno int(6) PRIMARY KEY AUTO_INCREMENT,
    passwd varchar(32) NOT NULL,
    date_created datetime NOt NULL,
    balance int)'''

cursor.execute(query)
db.commit()

query = '''alter table bank.users auto_increment=100000'''
cursor.execute(query)
db.commit()

query = '''create table if not exists bank.transactionhistory
(
    user1accno int(6),
    user2accno int(6),
    amount int not null,
    datetime datetime not null,
    FOREIGN KEY (user1accno) REFERENCES bank.users(accno)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (user2accno) REFERENCES bank.users(accno)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)'''

cursor.execute(query)
db.commit()

db.close()
