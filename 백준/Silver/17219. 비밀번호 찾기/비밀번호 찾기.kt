import java.io.BufferedReader
import java.io.InputStreamReader

fun main(){
    val br:BufferedReader = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().split(" ").map { it.toInt()}
    val lines = br.readLines()
    val map = HashMap<String, String>()
    val sb = StringBuilder()
    for(i in lines.indices){
        if(i<n[0]){
            val l = lines[i].split(" ")
            map[l[0]] = l[1]
        }else{
            sb.appendLine(map[lines[i]])
        }
    }
    print(sb)
}