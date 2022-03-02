from pyspark.sql.functions as F
from pyspark.sql import SparkSession,Row
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

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

df=spark.read.option("multiline","true").schema(schema).json("/home/maqsood/git-environment/myData/newData.json")
df.show(truncate=False)
df.printSchema()

df.select(df.name,F.split(df.currency,",").getItem(0)).show()


#from pyspark.sql.functions import explode
#dfFromTxt.select(dfFromTxt.name,dfFromTxt.currency._1).show(truncate=False)
#dfFromTxt.select (dfFromtxt("name"),dfFromTxt("currency"))
#Convert json column to multiple columns
#from pyspark.sql.functions import col,from_json




