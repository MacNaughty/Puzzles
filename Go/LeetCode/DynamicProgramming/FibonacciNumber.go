func fib(n int) int {
    if n < 2 {
        return n
    }
    
    n--
    
    last, current := 0, 1
    
    for n > 0 {
        current = last + current
        last = current - last
        n--
    }
    
    return current
}
