import pandas as pd
import mysql.connector as sqltor
import sys
# Connecting to MySQL using mysql.connector library
# conn=sqltor.connect(host="localhost",user="root",database="online_food",passwd="root")

def addUser(name, email, phone, password):
    conn=sqltor.connect(host="localhost",user="root",passwd="root",database="online_food")
    if conn.is_connected():
        # print("Connection Successful")
        mycur=conn.cursor()
        query = "INSERT INTO users (name, email, phone, password) VALUES ('{}','{}','{}','{}');".format(name, email, phone, password)
        mycur.execute(query)
        print("USER REGISTERED")
        conn.commit()
        conn.close()
    else:
        print("Connection Failure")
        sys.exit()
    