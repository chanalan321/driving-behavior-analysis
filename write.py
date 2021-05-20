import time
import mysql.connector
import json
import random
from datetime import datetime

def db_connection():
    mydb = mysql.connector.connect( host = 'comp123.cafkc5h3ic4r.us-east-1.rds.amazonaws.com',
	user = 'admin',
	port = '3306',
	database = 'comp123',
	passwd = 'password',
    autocommit = True)

    #print("successfully connect to the database")
    
    return mydb

mydb = db_connection()
cur = mydb.cursor()

def genData():
    driverID = "duxu1000009"
    speed = random.randint(0,140)
    now = datetime.now()
    timeNow = now.strftime('%Y-%m-%d %H:%M:%S')
    data = {}
    data['driverID'] = driverID
    data['speed'] = speed
    data['timeNow'] = timeNow
    return data

def execute():
    data = genData()
    print(data)
    sql = "insert into Monitor(driverID, speed, time) values ('{0}',{1},'{2}')".format(data['driverID'], data['speed'], data['timeNow'])
    print(sql)
    ret = cur.execute(sql)
    print("insert one record")

while True:   
    execute()
    time.sleep(1)