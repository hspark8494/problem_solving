import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    while (true){
        val line = br.readLine()!!
        if (line == "***") break
        println(line.reversed())
    }
}