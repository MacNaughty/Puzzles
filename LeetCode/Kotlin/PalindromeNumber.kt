/*
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Given an integer x, return true if x is palindrome integer.
*/

fun isPalindrome(x: Int): Boolean {
    var xCopy = x
    
    var reverseX = 0

    // From problem examples, if x is a negative palindrome (e.g. -101) return false
    // Otherwise, go through each digit of xCopy, from right to left, by taking remainder 10
    //  construct reverseX from left to right by multiplying reverseX by 10, and adding said remainder
    while (xCopy > 0) {
        reverseX = reverseX * 10 + xCopy.rem(10)
        xCopy /= 10
    }

    return x == reverseX
}



// Solution 1: convert to CharArray, simultaneously iterate through from left to right and from right to left
fun isPalindrome(x: Int): Boolean {
    if (x < 0) {
      return false
    }
  
    val xAsCharArray = x.toString().toCharArray()
    val lastIndex = xAsCharArray.size - 1

    var i = 0
    while (i < lastIndex - i) {
        if (xAsCharArray[i] != xAsCharArray[lastIndex - i]) {
            return false
        }
        i++
    }
    return true
}
