import java.util.*

fun main(){
    val li:PriorityQueue<Int> = PriorityQueue<Int>()
    for(x in 0 until readLine()!!.toInt()){
        val i = readLine()!!.toInt()
        if(i == 0){
            println(li.poll() ?: 0)
        }else{
            li.offer(i)
        }
    }

}
