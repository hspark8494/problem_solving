import java.io.*

var br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    val t = br.readLine()!!
    var odd = 0
    var even = 0

    br.readLine()!!.split(" ").forEach {
        if (it.toInt() % 2 == 0) {
            even++
        } else {
            odd++
        }
    }

    if ((odd - even == 1) || (odd - even == 0) ) {
        println(1)
    } else {
        println(0)
    }

}