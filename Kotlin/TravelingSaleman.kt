import kotlin.math.pow
import kotlin.math.sqrt

// 'destinations' and 'stops' will be used interchangably
fun travelingSalesman(destinations: Array<IntArray>, maxDistance: Double): Array<IntArray> {
    if (destinations.isEmpty()) {
        return arrayOf(intArrayOf())
    }

    val destinationsSize = destinations.size

    // distancesBetweenAllPointsArray is a 2D Array of doubles with size (destinationsSize^2 / 2)
    // valid indices are pairs (i, j) where 0 <= i < destinationsSize and 0 <= j < destinationsSize - i

    // for i == 0, distancesBetweenAllPointsArray[i][j] returns the distance between the origin and destinations[j]
    // for i > 0, distancesBetweenAllPointsArray[i][j] returns the distance between destinations[i-1] and destinations[j]
    
    val distancesBetweenAllStopsArray = Array<DoubleArray>(destinationsSize) { i ->
        DoubleArray(destinationsSize - i) { j ->
            if (i == 0) {
                val destination = destinations[j]
                val x = destination[0]
                val y = destination[1]
                kotlin.math.sqrt((x * x).toDouble() + (y * y).toDouble())
            } else {
                val point1 = destinations[i - 1]
                val point2 = destinations[i + j]
                kotlin.math.sqrt((point1[0] - point2[0]).toDouble().pow(2) + (point1[1] - point2[1]).toDouble().pow(2))
            }
        }
    }


    // This method must only to be called to calculate distances between points in destinations (not origin)
    fun findDistanceBetweenStopsByIndex(firstDestinationIndex: Int, secondDestinationIndex: Int): Double {
        return if (firstDestinationIndex < secondDestinationIndex) {
            val firstIndex = firstDestinationIndex + 1
            distancesBetweenAllStopsArray[firstIndex][secondDestinationIndex - firstIndex]
        } else {
            val firstIndex = secondDestinationIndex + 1
            distancesBetweenAllStopsArray[firstIndex][firstDestinationIndex - firstIndex]
        }
    }

    var optimalRouteIndexArray = intArrayOf()
    var optimalRouteSize = 0
    var optimalRouteDistance = maxDistance

    fun onNewOptimalRoute(newOptimalRoute: IntArray, newDistance: Double) {
        optimalRouteIndexArray = newOptimalRoute
        optimalRouteSize = newOptimalRoute.size
        optimalRouteDistance = newDistance
    }


    fun findOptimalRemainingRoute(
        currentRouteIndexArray: IntArray,
        currentRouteDistance: Double,
        lastStopDistanceFromOrigin: Double,
        remainingStopsIndexArray: IntArray
    ) {
        remainingStopsIndexArray.forEach { nextStopIndex ->
            val currentRouteSize = currentRouteIndexArray.size
            val nextStopDistanceFromOrigin = distancesBetweenAllStopsArray[0][nextStopIndex]
            val distanceBetweenLastStopAndNextStop = findDistanceBetweenStopsByIndex(currentRouteIndexArray.last(), nextStopIndex)

            val newRouteDistance = currentRouteDistance - lastStopDistanceFromOrigin + distanceBetweenLastStopAndNextStop + nextStopDistanceFromOrigin 
            if (newRouteDistance <= maxDistance) {
                val newRouteIndexArray = IntArray(currentRouteSize + 1) { i ->
                    if (i < currentRouteSize) {
                        currentRouteIndexArray[i]
                    } else {
                        nextStopIndex
                    }
                }
                var hasIterationReachedNewIndex = false
                val newRemainingStopIndexArray = IntArray(remainingStopsIndexArray.size - 1) { i ->
                    when {
                        hasIterationReachedNewIndex -> {
                            remainingStopsIndexArray[i + 1]
                        }
                        remainingStopsIndexArray[i] == nextStopIndex -> {
                            hasIterationReachedNewIndex = true
                            remainingStopsIndexArray[i + 1]
                        }
                        else -> {
                            remainingStopsIndexArray[i]
                        }
                    }
                }


                if (newRemainingStopIndexArray.isNotEmpty()) {
                    findOptimalRemainingRoute(
                        newRouteIndexArray,
                        newRouteDistance,
                        nextStopDistanceFromOrigin,
                        newRemainingStopIndexArray
                    )
                } else if (optimalRouteSize < destinationsSize || newRouteDistance < optimalRouteDistance) {
                    onNewOptimalRoute(newRouteIndexArray, newRouteDistance)
                }
            } else if (optimalRouteSize < currentRouteSize) {
                onNewOptimalRoute(currentRouteIndexArray, newRouteDistance)
            } else if ((optimalRouteSize == currentRouteSize) && (newRouteDistance < optimalRouteDistance)) {
                onNewOptimalRoute(currentRouteIndexArray, newRouteDistance)
            }
        }
    }

    for (i in 0 until destinationsSize) {
        val startingDistanceFromOrigin = distancesBetweenAllStopsArray[0][i]

        // If the distance from the origin to this point and back exceeds max distance, we have no need to try more routes
        if (startingDistanceFromOrigin * 2 > maxDistance) {
            continue
        }

        val currentRouteIndexArray = intArrayOf(i)
        val currentRouteDistance = startingDistanceFromOrigin * 2

        // remainingStopIndexArray is the relative complement of currentRouteIndexArray, w.r.t. (0 until destinationsSize)
        val remainingStopIndexArray = IntArray(destinationsSize - 1) { j ->
            if (j < i) {
                j
            } else {
                j + 1
            }
        }

        findOptimalRemainingRoute(currentRouteIndexArray, currentRouteDistance, startingDistanceFromOrigin, remainingStopIndexArray)
    }

    return if (optimalRouteIndexArray.isEmpty()) {
        arrayOf(optimalRouteIndexArray)
    } else {
        Array(optimalRouteIndexArray.size) { index ->
            destinations[optimalRouteIndexArray[index]]
        }
    }
}
