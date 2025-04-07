import pandas as pd
import mysql.connector as sqltor
import sys
# Connecting to MySQL using mysql.connector library
# conn=sqltor.connect(host="localhost",user="root",database="online_food",passwd="root")

def getRestaurantList():
    conn=sqltor.connect(host="localhost",user="root",passwd="root",database="online_food")
    if conn.is_connected():
        # print("Connection Successful")
        mycur=conn.cursor()
        mycur.execute("select * from restaurants;")
        result = mycur.fetchall()
        conn.close()
        return result
    else:
        print("Connection Failure")
        sys.exit()
    