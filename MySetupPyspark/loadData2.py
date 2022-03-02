from pyspark.sql import functions as F
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com")\
        .enableHiveSupport().getOrCreate()
#read json from text file
dfFromTxt=spark.read.json("/home/maqsood/Downloads/data.txt")
#df = dfFromTxt.select(
   # F.array(F.expr("results.*")).alias("results")
#)
dfFromTxt.printSchema()

