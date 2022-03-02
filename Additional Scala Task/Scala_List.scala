package com.test.scala

object Scala_List {
  def main(args: Array[String]): Unit =
  {
    val numbers = List(1, 2, 3, 4, 5, 7, 8,9, 11,13, 14, 12, 16)
    println("Original list is:")
    println(numbers)
    val even_nums = numbers.filter(_ % 2 ==0)
    println("Even number of the list:")
    println(even_nums)
    val odd_nums = numbers.filter(_ % 2 != 0)
    println("Odd number of the list:")
    println(odd_nums)
  }
}
