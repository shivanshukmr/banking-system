import os.path
import mysql.connector

pass_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "pass.txt")

with open(pass_path, "r") as f:
    output = f.readlines()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=output[0].strip("\n"),
    database="bank"
)


def get_DB():
    return db


def get_Cursor():
    return db.cursor()
