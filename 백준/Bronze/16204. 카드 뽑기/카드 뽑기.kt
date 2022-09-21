import kotlin.math.min

fun main(){
    val list = readLine()!!.split(" ").map { it.toInt() }
    print(min(list[1],list[2]) + min(list[0]-list[1], list[0]-list[2]))
}