import pandas as pd
import mysql.connector as sqltor
import sys
# Connecting to MySQL using mysql.connector library
# conn=sqltor.connect(host="localhost",user="root",database="online_food",passwd="root")

def addOrderItems(order_id, orders):
    conn=sqltor.connect(host="localhost",user="root",passwd="root",database="online_food")
    if conn.is_connected():
        # print("Connection Successful")
        mycur=conn.cursor()
        for key in orders:
            query = "INSERT INTO order_item (order_id, item_id, quantity) VALUES ({},{},{});".format(order_id, key, orders[key][2])
            print(query)
            mycur.execute(query)
        order_id = mycur.lastrowid
        conn.commit()
        conn.close()
        return order_id
    else:
        print("Connection Failure")
        sys.exit()
    