import java.lang.Integer.max
import java.util.Collections.min

fun main() {
    val n = readLine()!!.toInt()
    val price = readLine()!!.toInt()
    val li = mutableListOf<Int>()
    li.add(price)
    if (n>=5){
        li.add(price-500)
    }
    if (n>=10){
        li.add((price*0.9).toInt())
    }
    if(n>=15){
        li.add(price-2000)
    }
    if (n>=20){
        li.add((price*0.75).toInt())
    }
    println(max(0, min(li)))
}
