fun decentNumber(n: Int): Unit {
    when (n) {
        1, 2, 4, 7 -> {
            println(-1)
            return
        }
    }
    
    val remThree = n.rem(3)
    val dividend = n / 3
    
    val result = CharArray(n) { _ ->
        '5'
    }
    if (remThree == 0) {
        println(String(result))
        return
    } else {
        if (remThree == 1) {
        for (i in n-1 downTo n-10) {
            result[i] = '3'
        }
        println(String(result))
        return
        } else {
            // (remThree == 2)
            for (i in n-1 downTo n-5) {
                result[i] = '3'
            }
            println(String(result))
            return
        }
    }
}
