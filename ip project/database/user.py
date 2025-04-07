import pandas as pd
import mysql.connector as sqltor
import sys
# Connecting to MySQL using mysql.connector library
# conn=sqltor.connect(host="localhost",user="root",database="online_food",passwd="root")

def getUser(user_email, user_password):
    conn=sqltor.connect(host="localhost",user="root",passwd="root",database="online_food")
    if conn.is_connected():
        # print("Connection Successful")
        query  = "SELECT * FROM online_food.users where email='"+user_email+"' and password='"+user_password+"';"
        mycur=conn.cursor()
        mycur.execute(query)
        result = mycur.fetchall()
        conn.close()
        return result
    else:
        print("Connection Failure")
        sys.exit()