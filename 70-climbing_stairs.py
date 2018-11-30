func climbStairs(n int) int {
    var res int
    a, b := 1, 0
    
    for ; n > 0; n-- {
        res = a+b
        b, a = a, res
    }
    
    return res
}
