val dp = HashMap<Pair<Int, Int>, Boolean>()
val actions = arrayOf(Pair(1, 0), Pair(0, 1), Pair(3, 1), Pair(1, 3))

fun init() {
    dp[Pair(0, 0)] = true
    for (i in actions) {
        dp[i] = true
    }
}

fun main(args: Array<String>) {
    val (apple, banana) = readLine()!!.split(" ").map { it.toInt() }
    init()
    if (!(apple == 0 && banana == 0) && recur(Pair(apple, banana))) {
        println("Alice")
    } else {
        println("Bob")
    }
}

fun recur(curr: Pair<Int, Int>): Boolean {
    if (dp.containsKey(curr))
        return dp[curr]!!
    var result = false
    for (action in actions) {
        val next = Pair(curr.first - action.first, curr.second - action.second)
        if (next.first >= 0 && next.second >= 0 && !recur(next)) {
            result = true
            break
        }
    }
    dp[curr] = result
    return result
}