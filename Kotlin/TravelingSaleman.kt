import java.util.*
import kotlin.math.pow
import kotlin.math.sqrt

// 'destinations' and 'stops' will be used interchangably
fun travelingSalesman(destinations: Array<IntArray>, maxDistance: Double): Array<IntArray> {
    if (destinations.isEmpty()) {
        return arrayOf(intArrayOf())
    }

    val destinationsSize = destinations.size
    val allDestinationsIndexSet = Collections.unmodifiableSet(HashSet<Int>().apply {
        addAll(0 until destinationsSize)
    })

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
            distancesBetweenAllStopsArray[firstIndex][secondDestinationIndex - firstIndex]
        } else {
            val firstIndex = secondDestinationIndex + 1
            distancesBetweenAllStopsArray[firstIndex][firstDestinationIndex - firstIndex]
        }
    }

    var optimalRouteIndexArray = intArrayOf()
    var optimalRouteSize = 0
    var optimalRouteDistance = maxDistance

    fun updateOptimalRouteIfNeeded(newRoute: IntArray, newDistance: Double) {
        val newRouteSize = newRoute.size
        if (optimalRouteSize < newRouteSize || ((optimalRouteSize == newRouteSize) && (newDistance < optimalRouteDistance))) {
            optimalRouteIndexArray = newRoute
            optimalRouteSize = newRouteSize
            optimalRouteDistance = newDistance
        }
    }

    fun findOptimalRemainingRoute(
        currentRouteIndexArray: IntArray,
        currentRouteDistance: Double,
        lastStopDistanceFromOrigin: Double,
        remainingStopsIndexSet: Set<Int>
    ) {
        remainingStopsIndexSet.forEach { nextStopIndex ->

            val nextStopDistanceFromOrigin = distancesBetweenAllStopsArray[0][nextStopIndex]
            val distanceBetweenLastStopAndNextStop = findDistanceBetweenStopsByIndex(currentRouteIndexArray.last(), nextStopIndex)

            val newRouteDistance = currentRouteDistance - lastStopDistanceFromOrigin + distanceBetweenLastStopAndNextStop + nextStopDistanceFromOrigin
            if (newRouteDistance <= maxDistance) {
                val newRouteIndexArray = currentRouteIndexArray + nextStopIndex
                updateOptimalRouteIfNeeded(newRouteIndexArray, newRouteDistance)
                val newRemainingStopIndexSet = remainingStopsIndexSet.minus(nextStopIndex)

                if (newRemainingStopIndexSet.isNotEmpty()) {
                    findOptimalRemainingRoute(
                        newRouteIndexArray,
                        newRouteDistance,
                        nextStopDistanceFromOrigin,
                        newRemainingStopIndexSet
                    )
                }
            }
        }
    }

    for (i in 0 until destinationsSize) {
        val startingDistanceFromOrigin = distancesBetweenAllStopsArray[0][i]

        // If the distance from the origin to this point and back exceeds max distance, we have no need to try more routes
        val currentRouteDistance = startingDistanceFromOrigin * 2
        if (currentRouteDistance > maxDistance) {
            continue
        }

        findOptimalRemainingRoute(intArrayOf(i), currentRouteDistance, startingDistanceFromOrigin, allDestinationsIndexSet.minus(i))
    }

    return if (optimalRouteIndexArray.isEmpty()) {
        arrayOf(optimalRouteIndexArray)
    } else {
        Array(optimalRouteIndexArray.size) { index ->
            destinations[optimalRouteIndexArray[index]]
        }
    }
}
