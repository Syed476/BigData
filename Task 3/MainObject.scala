package com.test.scala


import scala.io.Source

object MainObject{
  def element_occurrences[A](list1:List[A]):Map[A, Int] = {
    list1.groupBy(el => el).map(e => (e._1, e._2.length))
  }
  def main(args:Array[String]){

    var finalList = List.empty[String]
    val filename = "Shakespeare.txt"
    val fileSource = Source.fromFile(filename)

    for(line<-fileSource.getLines){
      //println(line)
      var str : String = line
      val trimmedList: List[String] = str.split("[;:.,? ]").map(_.trim).toList
      finalList = List.concat(finalList, trimmedList)
      //println (finalList)
    }
    //println (finalList)
    println(element_occurrences(finalList))
    fileSource.close()
  }
}