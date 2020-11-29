import os.path
import mysql.connector

credentials_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "mysqlcredentials.txt"
)

with open(credentials_path, "r") as f:
    output = [word.strip("\n") for word in f.readlines()]

db = mysql.connector.connect(
    host=output[0],
    port=output[1],
    user=output[2],
    passwd=output[3],
    database="bank",
)


def get_DB():
    return db


def get_Cursor():
    return db.cursor()
