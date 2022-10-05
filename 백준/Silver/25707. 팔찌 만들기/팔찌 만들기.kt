import kotlin.math.absoluteValue

fun main() {
    val n = readLine()!!.toInt()
    val arr = readLine()!!.split(" ").map { it.toInt() }.toIntArray()
    arr.sort()
    var result = (arr.last() - arr[0]).absoluteValue
    for (i in 0 until n - 1) {
        result += (arr[i + 1] - arr[i]).absoluteValue
    }
    println(result)
}