import java.io.BufferedReader
import java.io.InputStreamReader

val br = BufferedReader(InputStreamReader(System.`in`))
val values = arrayOf(350.34, 230.90, 190.55, 125.30, 180.90)

fun main() {
    val n = br.readLine()!!.toInt()
    for (i in 0 until n) {
        val counts = br.readLine()!!.split(" ").map { it.toInt() }
        var result = 0.0
        for (j in 0 until 5) {
            result += values[j] * counts[j]
        }
        println("$%.2f".format(result))
    }
}