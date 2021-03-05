/*
This is my second (more elegant) solution for the same problem, using a CharArray for the result, rather than a StringBuilder

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
    // 5 and 3 can be treated as special cases (included in the following base case)
    when (n) {
        1, 2, 4, 7 -> {
            println(-1)
            return
        }
    }
    
    val remainderThree = n.rem(3)
    val dividend = n / 3
    
    // For the largest decent number we want as many 5's as possible, it's simply a question of how many trailing (i.e. rightmost) 5's to replace with 3's
    val result = CharArray(n) { _ ->
        '5'
    }

    if (remainderThree == 1) {
    // subtract 3 "555"s (representing 9) and add 2 "33333"s (representing 10) so difference is congruent to remainder (10 - 9) = 1  mod(3)
        for (i in n-1 downTo n-10) {
            result[i] = '3'
        }
    } else if (remainderThree == 2) {
        // subtract 2 "555"'s (representing 6) and add "33333" (representing 5) so  difference is congruent to remainder -1 = (5 - 6) = 2  mod(3)
        for (i in n-1 downTo n-5) {
            result[i] = '3'
        }
    }
    // We are finished, and can print the result, since the only remaining case is (remainderThree == 0), 
    //   and the CharArray was initialized with the desired result for this case 
    
    println(String(result))
    
}
