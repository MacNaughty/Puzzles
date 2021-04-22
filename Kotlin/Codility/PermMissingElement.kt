/*
An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.
Write a function:
  fun solution(A: IntArray): Int {
that, given an array A, returns the value of the missing element.

*/

fun solution(A: IntArray): Int {
    val aSize = A.size
    val cache = HashSet<Int>().apply {
        for (i in 1..(aSize + 1)) {
            add(i)
        }
    }

    A.forEach {
        cache.remove(it)
    }
    return cache.first()
}
