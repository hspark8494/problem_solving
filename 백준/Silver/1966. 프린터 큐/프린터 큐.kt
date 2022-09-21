import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main(){
    val br:BufferedReader = BufferedReader(InputStreamReader(System.`in`))
    repeat(br.readLine().toInt()){
        val l = br.readLine().split(" ")
        val que = LinkedList<Recode>(br.readLine().split(" ").mapIndexed { index, s -> Recode(index, s.toInt()) })
        val target:Recode = que[l[1].toInt()]
        var idx = 1
        while(!que.isEmpty()){
            val tmp = que.poll()
            if(check(que, tmp)){
                que.addLast(tmp)
            }else if(target == tmp){
                println(idx)
                break;
            }else{
                idx++
            }
        }
    }
}

fun check(li:List<Recode>, r:Recode):Boolean{
    for(i in li){
        if(r.data<i.data) return true
    }
    return false
}
data class Recode(var idx:Int, var data:Int)