package com.test.scala

object Scala_Occurrences {
  def elemnt_occurrences[A](list1:List[A]):Map[A, Int] = {
    list1.groupBy(el => el).map(e => (e._1, e._2.length))
  }

  def main(args: Array[String]): Unit = {
    println(elemnt_occurrences(List(1,1,1,2,2,3,6,4,5,6,4,6,1,4,2,6,2)))
  }
}
