/*
  Given a square grid of characters in the range ascii[a-z] rearrange elements of each row alphabetically, ascending. 
  Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
  
  https://www.hackerrank.com/challenges/grid-challenge/problem
*/
fun gridChallenge(grid: Array<String>): String {
    val gridSize = grid.size
  
    // Through some quick trial and error, realized that the 'square grid' is not actually square
    val stringLength = grid[0].length
    
    val sortedRowsAscendingGrid = Array<String>(gridSize) { i -> 
        String(grid[i].toCharArray().sortedArray())
    }
    
    for (i in 0 until stringLength) {
        for (j in 0 until gridSize - 1) {
            if (sortedRowsAscendingGrid[j][i] > sortedRowsAscendingGrid[j+1][i]) {
                return "NO"
            }
        }
    }
    return "YES"

}
