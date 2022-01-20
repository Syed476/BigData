from pyspark.sql import functions as F
from pyspark.sql import SparkSession,Row

spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com")\
        .enableHiveSupport().config("hive.metastore.uris","thrift://localhost:9083").getOrCreate()
#read json from text file


# Create Schema of the JSON column
from pyspark.sql.types import StructType,StructField, StringType
schema = StructType([ 
    StructField("geonameid",StringType(),True), 
    StructField("name",StringType(),True),
    StructField("code",StringType(),True),
    StructField("depends_on",StringType(),True),
    StructField("currency",StringType(),True),
    StructField("status",StringType(),True)
 ])

df=spark.read.option("multiline","true").json("hdfs://localhost:9000/myData/newData.json")

df.printSchema()
df.show(truncate=False)

from pyspark.sql.functions import explode
df.select(df.geonameid,explode(df.currency)).show(truncate=False)


df.write.mode("overwrite").saveAsTable("mydb.city_table")
df_sql = spark.sql("select * from mydb.city_table")


