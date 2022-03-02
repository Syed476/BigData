import pyspark

from pyspark.sql import SparkSession

def main():

	spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()

 	df = spark.read.csv('/home/maqsood/git-environment/myData/MOCK_DATA.csv',header=True,inferSchema='True')

	df.groupBy('gender').count().show()

	df.write.mode("overwrite").saveAsTable("mydb.test_table1")

	df_sql = spark.sql("select * from testdb.test_table1")

	df_sql.show()
main()
