# driving-behavior-analysis

This project is established with Flask, MySQL, Sprak and AWS. The frontend was developed with html. On the other hand, Flask was used to build backend, API server and router. MySQL was used to build the database. 

# project description

1. Generate a summary to show the driving behavior of each driver.
2. Monitor the driving speed of each driver in real time.

For 1), display the driving behavior information during the given period in a HTML table. The information should includes the car plate number, the cumulative number of times of overspeed and fatigue driving, the total time of overspeed and neutral slide.

For 2), use a diagram to visualize the driving speed of each driver during the given period. The diagram automatically updated every 30 seconds for monitoring the driving speed.

# Set up environment

## Set up database
SetUpDatabase.sql was used to set up both databases for function 1 and function 2.

## Analyze driver driving behavior
spark_select.py was used to analyze driver driving behavior since the data( detail-records ) is so big. Also, uploadDrivingBehavior.py was used to upload the result to mysql.

## Set up real-time monitoring device
Considering not having a real-time monitoring device, write.py is used to emulate it and generate data.

# Result

## home page:
<p align="center">
  <img src="https://github.com/chanalan321/driving-behavior-analysis/blob/a5cc543b91196c634b589460b511364ce9274cd8/photo/home.png">
</p>

## function 1:
<p align="center">
  <img src="https://github.com/chanalan321/driving-behavior-analysis/blob/a5cc543b91196c634b589460b511364ce9274cd8/photo/function%201.1.png">
</p>

## function 2:
<p align="center">
  <img src="https://github.com/chanalan321/driving-behavior-analysis/blob/a5cc543b91196c634b589460b511364ce9274cd8/photo/function%202.1.png">
</p>
