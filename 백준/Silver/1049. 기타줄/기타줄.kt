import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

val br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    var (n, m) = br.readLine()!!.split(" ").map { it.toInt() }
    var six = 1001
    var one = 1001
    for (i in 0 until m) {
        val (x, y) = br.readLine()!!.split(" ").map { it.toInt() }
        six = min(six, x)
        one = min(one, y)
    }
    if (six < one * 6) {
        var result = six * (n / 6)
        n %= 6
        result += if (six < one * n) six
        else one * n
        println(result)
    } else {
        print(one * n)
    }
}