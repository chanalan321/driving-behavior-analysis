from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime
import json
import time

application = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)


@application.route('/')
def home():
	return render_template('home.html')

@application.route('/drivingBehavior')
def student():
	return render_template('drivingBehavior.html')

@application.route('/drivingBehavior_summary',methods = ['POST', 'GET'])
def drivingBehavior_summary():
	if request.method == 'POST':
		startDay = request.form['startDay']
		startHour = request.form['startHour']
		startDay = datetime.strptime(startDay, '%Y-%m-%d')
		startDt = datetime(int(startDay.year), int(startDay.month) , int(startDay.day), int(startHour), 0, 0)

		endDay = request.form['endDay']
		endHour = request.form['endHour']
		endDay = datetime.strptime(endDay, '%Y-%m-%d')
		endDt = datetime(int(endDay.year), int(endDay.month) , int(endDay.day), int(endHour), 0, 0)

		mydb = db_connection()
		cur = mydb.cursor()
		info = "SELECT driverID,carPlateNumber,DATE(recordDAY),sum(rapidlySpeedup),sum(rapidlySlowdown),sum(neutralSlideINT),sum(neutralSlideFinished),sum( neutralSlideTime),sum(overspeed),sum(overspeedFinished),sum(overspeedTime),sum(fatigueDriving),sum(hthrottleStop),sum(oilLeak) FROM DrivingRecordA WHERE recordDAY BETWEEN '" + str(startDt) + "' AND '" + str(endDt) + "' GROUP BY driverID"
		cur.execute(info)

		myresult = cur.fetchall()
		return render_template("drivingBehavior_summary.html", results = myresult)

def db_connection():
	mydb = mysql.connector.connect( host = 'comp123.cafkc5h3ic4r.us-east-1.rds.amazonaws.com',
	user = 'admin',
	port = '3306',
	database = 'comp123',
	passwd = 'password')

	#print("successfully connect to the database")
	
	return mydb

@application.route("/monitor")
def index():
	driverID = request.args.get('driverID')
	if driverID: 
		return render_template("monitor.html", driverID = driverID)
	else: 
		return render_template("monitorForm.html")

@application.route("/data")
def getdata():
	mydb = db_connection()
	cur = mydb.cursor()
	driverID = request.args.get('driverID')
	if driverID: 
		sql = "SELECT time, speed FROM Monitor WHERE driverID = '%s'" %(driverID)

		cur.execute(sql)
		datas = []
		for i in cur.fetchall():
			timestamp = time.mktime(i[0].timetuple())
			datas.append([timestamp*1000, i[1]])

		if len(datas) > 0 :
			tmp_time = datas[-1][0]

		return json.dumps(datas)
	else:
		return ""

if __name__ == '__main__':
	application.run(port=5000, debug = True)

