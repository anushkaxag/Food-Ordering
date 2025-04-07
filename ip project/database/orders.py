import pandas as pd
import mysql.connector as sqltor
import sys
# Connecting to MySQL using mysql.connector library
# conn=sqltor.connect(host="localhost",user="root",database="online_food",passwd="root")

def placeOrder(user_id, restaurant_id, total, deliveryAddress):
    conn=sqltor.connect(host="localhost",user="root",passwd="root",database="online_food")
    if conn.is_connected():
        # print("Connection Successful")
        mycur=conn.cursor()
        query = "INSERT INTO Orders (user_id, restaurant_id, total, delivery_address) VALUES ({},{},{},'{}');".format(user_id, restaurant_id, total, deliveryAddress)
        mycur.execute(query)
        order_id = mycur.lastrowid
        conn.commit()
        conn.close()
        return order_id
    else:
        print("Connection Failure")
        sys.exit()
    