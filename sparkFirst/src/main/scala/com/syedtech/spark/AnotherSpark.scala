package com.syedtech.spark
import org.apache.spark.sql.SparkSession
import org.apache.spark.SparkConf
import org.apache.log4j.Logger
import org.apache.spark.SparkContext._
import org.apache.log4j.Level
import org.apache.spark._

object AnotherSpark {
  def main (args : Array [String])  {
    Logger.getLogger("org").setLevel((Level.ERROR))
    val conf = new SparkConf().setAppName("sparkCalculation").setMaster("local[3]")
    val sc = new SparkContext(conf)

    val tuple= List(("lily",23),("Jack",29),("James",21))
    val pairRDD = sc.parallelize(tuple)

    pairRDD.coalesce(1).saveAsTextFile("out/pair_rdd_from_tuple_list")
  }
}
