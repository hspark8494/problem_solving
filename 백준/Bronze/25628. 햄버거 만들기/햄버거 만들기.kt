import kotlin.math.min

fun main() {
    var (a, b) = readLine()!!.split(" ").map { it.toInt() }
    print(min(a/2, b))
}