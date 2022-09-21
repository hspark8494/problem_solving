import java.util.Scanner
import kotlin.math.min

fun main(){
    val sc = Scanner(System.`in`)
    val x:String = sc.next()
    val y:Int = sc.next()!!.toInt()
    val str = x.repeat(x!!.toInt())
    println(str.substring(0, min(y, str.length)))

}