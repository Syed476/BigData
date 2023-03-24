package com.BigData.spark.poc

import org.apache.spark.sql._
import org.apache.spark.sql.functions._

object testing {
  def main(args: Array[String]) {
    val spark = SparkSession.builder.master("local[*]").appName("testing").getOrCreate()
    //    val ssc = new StreamingContext(spark.sparkContext, Seconds(10))
    val sc = spark.sparkContext
    sc.setLogLevel("ERROR")
    import spark.implicits._
    import spark.sql
    val data = "/home/syed/Downloads/upload-pricequotes.csv"
    val df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(data)
    //df.show()
    df.createOrReplaceTempView("tab")
    val res = spark.sql("select * from tab where PRICE >2.0")
    res.show()
    spark.stop()
  }
}