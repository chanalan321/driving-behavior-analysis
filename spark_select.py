import os
import sys


from pyspark import SparkContext, SparkConf
from pyspark import SQLContext, Row
from pyspark.sql.types import *
from pyspark.sql.functions import lit

args = sys.argv
inp = args[1]
out = args[2]

sc = SparkContext()
sqlContext = SQLContext(sc)

text_file = sc.textFile(inp)

counts = text_file.map(lambda line: line.split(",")) \
             .filter(lambda line: len(line)>8)


wiki = counts.map(lambda p: Row(p[0], p[1], p[2], p[3]  \
            , p[4], p[5], p[6], p[7], p[8], p[9] \
                , p[10], p[11], p[12], p[13], p[14]\
                  , p[15], p[16], p[17], p[18]))


schemaString = "driverID carPlateNumber Latitude Longtitude  \
             Speed Direction siteName Time rapidlySpeedup rapidlySlowdown \
                 neutralSlide neutralSlideFinished neutralSlideTime overspeed overspeedFinished\
                     overspeedTime fatigueDriving hthrottleStop oilLeak"

fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)

schemaWiki = sqlContext.createDataFrame(wiki,schema)
df_with_x4 = schemaWiki.withColumn("reportID",lit(inp))
df_with_x4.registerTempTable("wikistats")

group_res = sqlContext.sql("SELECT first(reportID),first(driverID),first(carPlateNumber),first(Time) as recordDAY,HOUR(Time) as recordHOUR,sum(rapidlySpeedup),sum(rapidlySlowdown),sum(neutralSlide),sum(neutralSlideFinished),\
                            sum(neutralSlideTime),sum(overspeed),sum(overspeedFinished),sum(overspeedTime),sum(fatigueDriving),\
                            sum(hthrottleStop),sum(oilLeak) FROM wikistats GROUP BY driverID,DAY(Time),HOUR(Time)")

group_res.coalesce(1).write.csv(out)

sc.stop()
