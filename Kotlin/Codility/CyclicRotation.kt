/*
An array A consisting of N integers is given. 
Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:
  fun solution(A: IntArray, K: Int): IntArray
that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
*/



fun solution(A: IntArray, K: Int): IntArray {


    if (A.isEmpty() || K == 0) {
         return A
    }
    val arraySize = A.size
    if (arraySize == 1 || (K.rem(arraySize) == 0)) {
        return A
    }

    var i = if (K > arraySize) {
        K.rem(arraySize)
    } else {
        K
    }

    var currentElement = A[i]
    A[i] = A[0]

    var numSwapCount = 1

    while (numSwapCount < arraySize) {
        val j = if (i + K >= arraySize) {
            (i + K).rem(arraySize)
        } else {
            i + K
        }

        val nextElement = A[j]
        A[j] = currentElement
        currentElement = nextElement
        i = j
        numSwapCount++
    }

    return A
}
