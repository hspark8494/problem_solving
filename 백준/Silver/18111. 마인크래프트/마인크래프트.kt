import java.io.BufferedReader
import java.io.InputStreamReader

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val l = br.readLine().split(" ").map{ it.toInt()}
    val li = ArrayList<Int>(l[0]*l[1])
    for(i in 0 until l[0].toInt()){
        li.addAll(br.readLine().split(" ").map { it.toInt() })
    }
    var depth = 0
    var rSec = Int.MAX_VALUE

    loop@ for(i in li.maxOrNull()!! downTo 0){
        var blocks = l[2]
        var sec = 0
        var down = 0
        for(x in li){
            var t = x-i
            if(t>0){
                sec += t * 2
                blocks += t
            }else if(t<0) {
                down += (-t)
            }

        }
        sec += down
        blocks -= down
        if(sec<=rSec && blocks >= 0) {
            depth = if(sec == rSec){
                depth.coerceAtLeast(i)
            }else{
                i
            }
            rSec = sec
        }
    }
    println("$rSec $depth")
}