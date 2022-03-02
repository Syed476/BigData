package com.test.scala

object Sum_Product {
  def main(args: Array[String]): Unit =
  {
    //Iterate over given list
    val numbers = List(1, 3, 5, 7, 9,4,8)
    println("Iterate over a list:")
    for( i <- numbers)
    {
      println(i)
    }

    println("Sum all the items of the list:")
    //Applying sum method on list
    val result = numbers.sum
    println(result)

    println("Multiplies all the items of the list:")
    val result1 = numbers.product
    println(result1)
  }
}
