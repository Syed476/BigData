from pyspark.sql import functions as F
from pyspark.sql import SparkSession,Row


spark = SparkSession.builder.master("local[1]").appName("hdfstospark.com")\
        .enableHiveSupport().config("hive.metastore.uris","thrift://localhost:9083").getOrCreate()

#Read data from data1
df1=spark.read.option("multiline","true").json("hdfs://localhost:9000/myData/cricketUpdate.json")
df1=df1.select(df1.venue,df1.date,df1.match_title,df1.status)
#df1.printSchema()
#df1.show()

#Read data from data2
df2=spark.read.option("multiline","true").json("hdfs://localhost:9000/myData/cricketUpdate1.json")

from pyspark.sql.functions import explode
df2 = df2.withColumnRenamed("startDate", "date")
df2=df2.select(df2.date,df2.endDate,df2.slug)
#df2.printSchema()
#df2.show()

# Joining the df1 and df2
df = df1.join(df2, on=['date'], how='outer')
df.printSchema()
df=df.select(df.match_title,df.slug,df.date)
df.show()

# Saving data to Hive tablepip install matplotlib
df.write.mode("overwrite").saveAsTable("mydb.cricket_fixtures")
df_sql = spark.sql("select * from mydb.cricket_fixtures")

# Read nested team data from json data2
# Read data from json data2
teams_df=spark.read.option("multiline","true").json("hdfs://localhost:9000/myData/cricketUpdate1.json")
teams_df.printSchema()
teams_df=teams_df.withColumn("teams",F.explode(F.col("teams"))).select("teams.score","teams.isHome","teams.isLive")

#teams_df.printSchema()
#teams_df.show()

pandasDF = teams_df.toPandas()
print(pandasDF)

# Saving data to Hive table
df.write.mode("overwrite").saveAsTable("mydb.team_scores")
df_sql = spark.sql("select * from mydb.teams_df")
