import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com")\
        .enableHiveSupport().config("hive.metastore.uris","thrift://localhost:9083").getOrCreate()
#spark.sql("use mydb")
df = spark.read.csv('/home/maqsood/git-environment/myData/MOCK_DATA.csv',header=True,inferSchema=True)
df.show(10)
df.printSchema()
df.groupBy('gender').count().show()
df.write.mode("overwrite").saveAsTable("mydb.test_table")
df_sql = spark.sql("select * from mydb.test_table")
