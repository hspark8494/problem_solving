import java.util.*

fun main(){
    val li:PriorityQueue<Int> = PriorityQueue<Int>(kotlin.Comparator { o1, o2 -> -(o1-o2) })

    for(x in 0 until readLine()!!.toInt()){
        val i = readLine()!!.toInt()
        if(i == 0){
            println(li.poll() ?: 0)
        }else{
            li.offer(i)
        }
    }

}
