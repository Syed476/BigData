from pyspark.sql import functions as F
from pyspark.sql import SparkSession,Row

spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com")\
        .enableHiveSupport().config("hive.metastore.uris","thrift://localhost:9083").getOrCreate()
#read json from text file


# Create Schema of the JSON column
from pyspark.sql.types import StructType,StructField, StringType

df=spark.read.option("multiline","true").json("hdfs://localhost:9000/myData/dataUpdate.json")

df.printSchema()

cities_df=df.withColumn("cities",F.explode(F.col("cities"))).select("cities.*")
cities_df.show()



