import java.io.*

var br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    var n = br.readLine()!!.toInt()
    var mx = 0
    for (i in 0 until n) {
        var (a, d, g) = br.readLine()!!.split(" ").map { it.toInt() }
        mx = maxOf(mx, getScore(a, d, g))
    }
    println(mx)
}

fun getScore(a:Int, d:Int, g:Int):Int{
    var score = a*(d+g)
    if(a==d+g){
        score *= 2
    }
    return score
}