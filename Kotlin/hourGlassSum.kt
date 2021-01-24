fun hourglassSum(arr: Array<Array<Int>>): Int {
    var max = Int.MIN_VALUE
    for ((indexI, arrayValueI) in arr.withIndex()) {
        if (indexI + 2 < arr.size) {
            for ((indexJ, valueJ) in arrayValueI.withIndex()) {
                if (indexJ + 2 < arrayValueI.size) {
                    val topSum = valueJ + arrayValueI[indexJ + 1] + arrayValueI[indexJ + 2]
                    val mid = arr[indexI + 1][indexJ + 1]
                    val bottomSum = arr[indexI + 2][indexJ] + arr[indexI + 2][indexJ + 1] + arr[indexI + 2][indexJ + 2]
                    max = kotlin.math.max(topSum + mid + bottomSum, max)
                }
            }

        }

    }

    return max
}

fun main(args: Array<String>) {

    val scan = Scanner(System.`in`)

    val arr = Array<Array<Int>>(6, { Array<Int>(6, { 0 }) })

    for (i in 0 until 6) {
        arr[i] = scan.nextLine().split(" ").map{ it.trim().toInt() }.toTypedArray()
    }

    val result = hourglassSum(arr)

    println(result)
}
