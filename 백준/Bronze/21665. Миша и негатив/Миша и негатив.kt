import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    val (h, w) = br.readLine()!!.split(" ").map { it.toInt() }
    val a = Array(h) { br.readLine()!!.toCharArray() }
    br.readLine()
    val b = Array(h) { br.readLine()!!.toCharArray() }
    var result = 0
    for (i in 0 until h){
        for (j in 0 until w){
            if (a[i][j] == b[i][j]){
                result += 1
            }
        }
    }
    println(result)
}