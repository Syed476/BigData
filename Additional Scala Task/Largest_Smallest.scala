package com.test.scala

object Largest_Smallest {
  def main(args: Array[String]): Unit =
  {
    //Iterate over a list
    val nums = List( 3, 5, 7,22, 9, 11, 1,14, 12)
    println("Original list:")
    println(nums)
    println("Largest number of the given list:")
    println(nums.max)
    println("Smallest number from the given list:")
    println(nums.min)
  }
}
