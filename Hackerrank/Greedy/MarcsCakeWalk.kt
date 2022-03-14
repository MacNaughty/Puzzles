/*
 If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least 2^j * c miles to maintain his weight.
 Given an array of integers, calorie, representing calories of respective cupcakes, determine the minimum distance Marc must walk to burn off all the calories
*/

// Minimum distance will be from eating the calories with the most calories first (i.e. descending order of calories)
fun marcsCakewalk(calorie: Array<Int>): Long {
    calorie.sortDescending()
    var result = calorie[0].toLong()
    for (i in 1 until calorie.size) {
        result += (Math.pow(2.0, i.toDouble()) * calorie[i]).toLong()
    }
    return result
}
