import kotlin.math.*
import java.util.Scanner

fun main(){
    val sc = Scanner(System.`in`)
    for(i in 1..sc.nextInt()){
        val arr = Array<Int>(sc.nextInt()){sc.nextInt()}.sorted()
        var gap:Int = 0

        for(i in 0..arr.size-2){
            gap = max(abs(arr[i]-arr[i+1]),gap)
        }
        println("Class $i\nMax ${arr.last()}, Min ${arr.first()}, Largest gap $gap")
    }
}
