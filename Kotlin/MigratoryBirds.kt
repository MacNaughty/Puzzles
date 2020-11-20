import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

// Complete the migratoryBirds function below.
fun migratoryBirds(arr: Array<Int>): Int {

    var idWithHighestCount = 0
    var highestCount = 0

    val birdUUIDCountMap: HashMap<Int, Int> = HashMap<Int, Int>()
    for (id in arr) {
        val a = birdUUIDCountMap[id]
        if (a == null) {
            birdUUIDCountMap[id] = 1
        } else {
            val newIdCount = a + 1
            birdUUIDCountMap[id] = newIdCount
            if ((newIdCount > highestCount) || ((newIdCount == highestCount) && (id < idWithHighestCount))) {
                highestCount = newIdCount
                idWithHighestCount = id
            }
        }
    }

    return idWithHighestCount

}

fun main(args: Array<String>) {
    val arrCount = readLine()!!.trim().toInt()

    val arr = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val result = migratoryBirds(arr)

    println(result)
}
