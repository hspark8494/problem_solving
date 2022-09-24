import java.io.*
import kotlin.math.max

val br = BufferedReader(InputStreamReader(System.`in`))
fun main(args: Array<String>) {
    val (a, b) = br.readLine()!!.split(" ")
    var mx = -1
    for (i in 0..b.length - a.length) {
        var eq = 0
        for (j in a.indices) {
            if (a[j] == b[i + j]) {
                eq += 1
            }
        }
        mx = max(mx, eq)
    }
    println(b.length - mx - (b.length - a.length))
}