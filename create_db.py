import mysql.connector
import os

database = os.getenv("DB_DATABASE")


def create_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in my_cursor]
    if database not in databases:
        my_cursor.execute("CREATE DATABASE " + database)
