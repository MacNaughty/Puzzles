/*
This is my first solution for the problem. While tidying up I realized there was a better solution using a CharArray (in same parent directory as this file).
Problem: 

A Decent Number has the following properties:
    1. Its digits can only be 3's and/or 5's.
    2. The number of 3's it contains is divisible by 5.
    3. The number of 5's it contains is divisible by 3.
    4. It is the largest such number for its length.
Given an integer n, where 1 <= n <= 100000
Find the decent number for n
https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem?isFullScreen=false&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
*/


fun decentNumber(n: Int): Unit {
    // Having seen a similar problem in school, 
    // For any integer m > 7, there exists integers x & y such that 5*x + 3*y = m
    // 5 and 3 can be treated as special cases
    when (n) {
        1 , 2, 4, 7 -> println(-1)
        return
    }
    
    // The largest such number will contain as many leading 5's as possible
    val remainderThree = n.rem(3)
    val dividend = n / 3
    
    val stringBuilder = StringBuilder()
    if (remainderThree == 0) {
        // We can simply use all 5's, added in triplets for efficiency
        for (i in 1..dividend) {
            stringBuilder.append("555")
        }
    } else if (remainderThree == 1) {
        // All 5's, other than the end: 
        // subtract 3 "555"'s (representing 9) and add 2 "33333" (representing 10) so difference is congruent to remainder (9 - 10) = 1 mod(3)
        for (i in 1..(dividend - 3)) {
            stringBuilder.append("555")
        }
        stringBuilder.append("3333333333")
    } else {
        // (remainderThree == 2)
        // All 5's, other than the end: 
        // subtract 2 "555"'s (representing 6) and add "33333" (representing 5) so difference is congruent to remainder -1 = (5 - 6) = 2  mod(3)
        for (i in 1..(dividend - 1)) {
            stringBuilder.append("555")
        }
        stringBuilder.append("33333")
    }
    
    println(stringBuilder.toString())
}
