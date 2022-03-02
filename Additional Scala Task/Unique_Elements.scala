package com.test.scala

object Unique_Elements {
  def main(args: Array[String]): Unit =
  {
    val nums = List(1, 3, 5,3,3,3 ,2,13, 7, 9, 11,9, 5,5,5, 2,77, 14, 12, 3)
    println("Original list of numbers:")
    println(nums)
    val result1 = nums.distinct
    println("Unique elements of the list:")
    println(result1)

  }
}
