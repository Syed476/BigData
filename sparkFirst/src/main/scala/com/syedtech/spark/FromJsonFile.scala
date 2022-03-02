package com.syedtech.spark


import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions
import org.apache.spark.sql.types._

object FromJsonFile {
  def main(args:Array[String]): Unit = {
    val spark: SparkSession = SparkSession.builder()
      .master("local[3]")
      .appName("SparkByExample")
      .getOrCreate()



    val df_with_schema = spark.read.json("/home/maqsood/Downloads/data.txt")
    df_with_schema.printSchema()

  }
}
