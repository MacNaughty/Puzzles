/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
*/

/*
This question is in the dynamic programming category, but has a greedy solution.
O(n) time complexity, O(1) space complexity
*/


fun maxProfit2(prices: IntArray): Int {
    val pricesSize = prices.size
    if (pricesSize == 1) return 0

    var minPriceSoFar = prices[0]
    var result = 0

    for (i in 1 until pricesSize) {
        result = max(result, prices[i] - minPriceSoFar)
        minPriceSoFar = min(minPriceSoFar, prices[i])
    }

    return result
}
