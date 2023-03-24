from pyspark.sql import *
from pyspark.sql.functions import *
spark=SparkSession.builder.master("local[*]").appName("test").getOrCreate()
# data="/home/syed/Downloads/upload-pricequotes.csv"
data="hdfs://localhost:9000/datasets/upload-pricequotes.csv"
df= spark.read.format("csv").option("header","true").option("inferSchema","true").load(data)
# df.show()

df_sales=df.filter(df.BASE_PRICE > 1.5)
df_sales.show()