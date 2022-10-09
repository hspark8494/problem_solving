import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    for (i in 0 until br.readLine().toInt()) {
        var result = 0
        for (s in br.readLine()!!){
            if (s == 'D'){
                break
            }else{
                result++
            }
        }
        println(result)
    }
}