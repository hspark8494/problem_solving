import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
fun main(args: Array<String>) {
    val (a,b) = br.readLine()!!.split(" ").map { it.toInt() }
    val ax = 100-a
    val bx = 100-b
    val q = (ax*bx)/100
    val r = (ax*bx)%100
    println("$ax $bx ${100-ax-bx} ${ax*bx} $q $r")
    println("${100-ax-bx+q} $r")
}