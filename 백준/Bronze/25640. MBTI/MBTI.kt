import java.io.BufferedReader
import java.io.InputStreamReader

var br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    val t = br.readLine()!!
    val n = br.readLine()!!.toInt()
    var result = 0
    for (i in 0 until n) {
        if (t == br.readLine()!!) {
            result ++
        }
    }
    print(result)
}