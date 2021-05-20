# Load the Pandas libraries with alias 'pd' 
import pandas as pd
import mysql.connector

def db_connection():
	mydb = mysql.connector.connect( host = 'comp4442-lab3.cafkc5h3ic4r.us-east-1.rds.amazonaws.com',
	user = 'admin',
	port = '3306',
	database = 'gp',
	passwd = 'hahaIam87',) #/////

	#print("successfully connect to the database")
	
	return mydb
list_data = []

data1 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_02_08_00_00.csv") 
data2 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_03_08_00_00.csv") 
data3 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_04_08_00_00.csv") 
data4 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_05_08_00_00.csv") 
data5 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_06_08_00_00.csv") 
data6 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_07_08_00_00.csv") 
data7 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_08_08_00_00.csv") 
data8 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_09_08_00_00.csv") 
data9 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_10_08_00_00.csv") 
data10 = pd.read_csv("C:/Users/alan/Desktop/COMP4442-Project/result/detail_record_2017_01_11_08_00_00.csv") 

list_data.append(data1)
list_data.append(data2)
list_data.append(data3)
list_data.append(data4)
list_data.append(data5)
list_data.append(data6)
list_data.append(data7)
list_data.append(data8)
list_data.append(data9)
list_data.append(data10)

mydb = db_connection()
mycursor = mydb.cursor()
#data1 = data.astype(object).where(pd.notnull(data), "")
for i in range(len(list_data)):
	data_all1 = list_data[i].where(pd.notnull(list_data[i]), None)
	data_all2 = data_all1.values.tolist()
	sql = 'REPLACE INTO DrivingRecordA (reportID,driverID,carPlateNumber,recordDAY,rapidlySpeedup,rapidlySlowdown,neutralSlideINT,neutralSlideFinished,neutralSlideTime,overspeed,overspeedFinished,overspeedTime,fatigueDriving,hthrottleStop,oilLeak) values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s);'

	mycursor.executemany(sql, data_all2)
	mydb.commit()

'''
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
'''
mycursor.close()