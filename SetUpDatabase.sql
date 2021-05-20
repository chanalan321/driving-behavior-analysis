CREATE DATABASE gp;
USE gp;
CREATE TABLE IF NOT EXISTS DrivingRecordA
(
reportID varchar(255) NOT NULL,
driverID varchar(40) NOT NULL,
carPlateNumber varchar(40) DEFAULT NULL,
recordDAY DATETIME NOT NULL,
rapidlySpeedup INT DEFAULT NULL,
rapidlySlowdown INT DEFAULT NULL,
neutralSlideINT INT DEFAULT NULL,
neutralSlideFinished INT DEFAULT NULL,
neutralSlideTime INT DEFAULT NULL,
overspeed INT DEFAULT NULL,
overspeedFinished INT DEFAULT NULL,
overspeedTime INT DEFAULT NULL,
fatigueDriving  INT DEFAULT NULL,
hthrottleStop  INT DEFAULT NULL,
oilLeak  INT DEFAULT NULL,
PRIMARY KEY (reportID,driverID,recordDAY)
) ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE IF NOT EXISTS Monitor
(
driverID varchar(20) NOT NULL,
speed INT,
time datetime
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SELECT * from Monitor;
SELECT * from DrivingRecordA;