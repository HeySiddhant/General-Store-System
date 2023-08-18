import mysql.connector

mydb = None


def get_sql_connection():
    print("Opening mysql connection")
    global mydb

    if mydb is None:
        mydb = mysql.connector.connect(user='root', password='siddhant', database='grocery_store')

    return mydb
