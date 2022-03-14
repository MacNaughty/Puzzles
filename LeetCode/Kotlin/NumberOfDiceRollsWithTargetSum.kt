/*
You have d dice and each die has f faces numbered 1, 2, ..., f.
Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to roll the dice so the sum of the face-up numbers equals target.

*/


fun numRollsToTarget(d: Int, f: Int, target: Int): Int {
  
    // Base cases
    if (d*f < target) {
        return 0
    } else if ((d == 1 && f >= target) || (d*f == target)) {
        return 1
    }

    
    var cache = IntArray(target+1)
    cache[0] = 1

    for (i in 0 until d) {
        val temp = IntArray(target+1)
        for (j in 1..f) {
            for (k in j..target) {
                temp[k] = (temp[k] + cache[k - j]) % 1000000007
            }
        }
        cache = temp
    }

    return cache[target]
}
