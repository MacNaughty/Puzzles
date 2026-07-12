var reverse = function(x) {
    if (x > -10 && x < 10) {
        return x
    }

    isNegative = false
    if (x < 0) {
        isNegative = true
        x *= -1
    }

    let max = 0
    if (isNegative) {
        max = 0x80000000
    } else {
        max = 0x7fffffff
    }

    let result = 0
    while (x > 0) {
        let nextStep = x % 10
        let nextResult = result*10+nextStep
        if (nextResult > max) {
            return 0
        } else {
            result = nextResult
            x = Math.floor(x/10)
        }
    }
    if (isNegative) {
        return result*-1
    } else {
        return result
    }
};
