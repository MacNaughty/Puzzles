fun travelingSalesman(destinations: Array<IntArray>, maxDistance: Double): Array<IntArray> {
    if (destinations.isEmpty()) {
        return arrayOf(intArrayOf())
    }

    val destinationsSize = destinations.size
    
    // Originally used a set as the collection that tracked remaining stop indices, but current solution uses IntArray instead.
    //    So allDestinationsIndexSet is currently not being used, but leaving it as a reminder because I think it has potential to be better
    val allDestinationsIndexSet = Collections.unmodifiableSet(HashSet<Int>(destinationsSize).apply {
        addAll(0 until destinationsSize)
    })

    // distancesBetweenAllPointsArray is a 2D Array of doubles
    // for all pairs of indices (i, j) where 0 <= i < destinationsSize and 0 <= j < destinationsSize - i
    // size (n^2 / 2)
    // for i > 0, distancesBetweenAllPointsArray[i][j] returns the distance between destinations[i-1] and destinations[j]
    // for i == 0 , distancesBetweenAllPointsArray[i][j] returns the distance between the origin and destinations[j]
    val distancesBetweenAllPointsArray = Array<DoubleArray>(destinationsSize) { i ->
        DoubleArray(destinationsSize - i) { j ->
            if (i == 0) {
                val destination = destinations[j]
                val x = destination[0]
                val y = destination[1]
                sqrt((x * x).toDouble() + (y * y).toDouble())
            } else {
                val point1 = destinations[i - 1]
                val point2 = destinations[i + j]
                sqrt((point1[0] - point2[0]).toDouble().pow(2) + (point1[1] - point2[1]).toDouble().pow(2))
            }
        }
    }


    // This method must only to be called to calculate distances between points in destinations (not origin)
    fun findDistanceBetweenStopsByIndex(firstDestinationIndex: Int, secondDestinationIndex: Int): Double {
        return if (firstDestinationIndex < secondDestinationIndex) {
            val firstIndex = firstDestinationIndex + 1
            distancesBetweenAllPointsArray[firstIndex][secondDestinationIndex - firstIndex]
        } else {
            val firstIndex = secondDestinationIndex + 1
            distancesBetweenAllPointsArray[firstIndex][firstDestinationIndex - firstIndex]
        }
    }

    var optimalRouteByIndex = intArrayOf()
    var optimalRouteSize = 0
    var optimalRouteDistance = maxDistance

    fun onNewOptimalRoute(newOptimalRoute: IntArray, newDistance: Double) {
        optimalRouteByIndex = newOptimalRoute
        optimalRouteSize = newOptimalRoute.size
        optimalRouteDistance = newDistance
    }

    fun findBestRemainingRoute(
        currentRouteIndexArray: IntArray,
        currentRouteDistance: Double,
        lastStopDistanceFromOrigin: Double,
        remainingStopIndexArray: IntArray
    ) {
        remainingStopIndexArray.forEach { nextStopIndex ->
            val currentRouteSize = currentRouteIndexArray.size
            val nextStopDistanceFromOrigin = distancesBetweenAllPointsArray[0][nextStopIndex]
            val distanceBetweenLastStopAndNextStop = findDistanceBetweenStopsByIndex(currentRouteIndexArray.last(), nextStopIndex)

            val newRouteDistance =
                currentRouteDistance - lastStopDistanceFromOrigin + nextStopDistanceFromOrigin + distanceBetweenLastStopAndNextStop
            if (newRouteDistance <= maxDistance) {
                val newRouteByIndex = IntArray(currentRouteSize + 1) { i ->
                    if (i < currentRouteSize) {
                        currentRouteIndexArray[i]
                    } else {
                        nextStopIndex
                    }
                }
                var hasIterationReachedNewIndex = false
                val newRemainingStopIndices = IntArray(remainingStopIndexArray.size - 1) { i ->
                    if (hasIterationReachedNewIndex) {
                        remainingStopIndexArray[i+1]
                    } else {
                        val currentStopIndex = remainingStopIndexArray[i]
                        if (currentStopIndex != nextStopIndex) {
                            currentStopIndex
                        } else {
                            hasIterationReachedNewIndex = true
                            remainingStopIndexArray[i+1]
                        }
                    }
                }

                if (newRemainingStopIndices.isNotEmpty()) {
                    findBestRemainingRoute(
                        newRouteByIndex,
                        newRouteDistance,
                        nextStopDistanceFromOrigin,
                        newRemainingStopIndices
                    )
                } else if (optimalRouteSize < destinationsSize || newRouteDistance < optimalRouteDistance) {
                    onNewOptimalRoute(newRouteByIndex, newRouteDistance)
                }
            } else if (optimalRouteSize < currentRouteSize) {
                onNewOptimalRoute(currentRouteIndexArray, newRouteDistance)
            } else if ((optimalRouteSize == currentRouteSize) && (newRouteDistance < optimalRouteDistance)) {
                onNewOptimalRoute(currentRouteIndexArray, newRouteDistance)
            }
        }
    }


    for (i in 0 until destinationsSize) {
        val startingPointDistanceFromOrigin = distancesBetweenAllPointsArray[0][i]

        // Can probably be generalized
        if (startingPointDistanceFromOrigin * 2 > maxDistance) {
            continue
        }

        val currentRouteByIndex = intArrayOf(i)
        var currentRouteDistance = startingPointDistanceFromOrigin * 2

        // currentRouteIndicesRemaining is the relative complement of currentRouteByIndex, w.r.t. allDestinationsIndexSet
        val remainingStopIndices = IntArray(destinationsSize - 1) { j ->
            if (j < i) {
                j
            } else {
                j+1
            }
        }

        findBestRemainingRoute(currentRouteByIndex, currentRouteDistance, startingPointDistanceFromOrigin, remainingStopIndices)

    }

    return if (optimalRouteByIndex.isEmpty()) {
        arrayOf(optimalRouteByIndex)
    } else {
        Array<IntArray>(optimalRouteByIndex.size) { index ->
            destinations[optimalRouteByIndex[index]]
        }
    }

}
