import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
fun main(){
    val (cw, ch, sw, sh) = br.readLine()!!.split(" ").map { it.toInt() }
    println(if ((cw-sw>=2) && (ch-sh>=2)) 1 else 0)
}