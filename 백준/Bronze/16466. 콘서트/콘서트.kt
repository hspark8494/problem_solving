import java.io.BufferedReader
import java.io.InputStreamReader

fun main(){
    val br:BufferedReader = BufferedReader(InputStreamReader(System.`in`))
    br.readLine()
    val li = br.readLine().split(" ").map{it.toInt()}.sorted()
    var idx = 1
    var r = 1
    while(true){
        if(idx>=li.size||(r != li[idx-1] && r!=li[idx])){
            break;
        }else if(r>=li[idx]){
            idx++
        }
        r++
    }
    print(r)
}