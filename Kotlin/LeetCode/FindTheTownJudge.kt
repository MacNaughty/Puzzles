fun findJudge(N: Int, trust: Array<IntArray>): Int {
    if (N == 1 && trust.isEmpty()) {
        return 1
    }

    val stats = IntArray(N+1)

    trust.forEach {
        stats[it[0]]--
        stats[it[1]]++
    }

    stats.forEachIndexed { i, v ->
        if (v == N - 1) {
            return i
        }
    }

    return -1
}
