import pandas as pd
import mysql.connector as sqltor
import sys
# Connecting to MySQL using mysql.connector library
# conn=sqltor.connect(host="localhost",user="root",database="online_food",passwd="root")

def getDishesByRestaurant(restaurant_id):
    conn=sqltor.connect(host="localhost",user="root",passwd="root",database="online_food")
    if conn.is_connected():
        # print("Connection Successful")
        query  = "select * from items where restaurant_id ="+restaurant_id+";"
        mycur=conn.cursor()
        mycur.execute(query)
        result = mycur.fetchall()
        conn.close()
        return result
    else:
        print("Connection Failure")
        sys.exit()
    