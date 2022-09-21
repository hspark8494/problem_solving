import java.util.*
import kotlin.math.abs

fun main(){
    val li:PriorityQueue<Int> = PriorityQueue<Int>(kotlin.Comparator { o1, o2 -> val x = abs(o1)-abs(o2); if(x==0) o1-o2 else x })

    for(x in 0 until readLine()!!.toInt()){
        val i = readLine()!!.toInt()
        if(i == 0){
            println(li.poll() ?: 0)
        }else{
            li.offer(i)
        }
    }

}
