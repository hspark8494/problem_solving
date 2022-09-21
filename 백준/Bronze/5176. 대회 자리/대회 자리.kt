import java.util.Scanner

fun main(){
    val sc = Scanner(System.`in`)
    for(x in 0 until sc.nextInt()){
        val p = sc.nextInt()
        var r = 0
        val m = List(sc.nextInt()){1}.toMutableList()
        for(i in 0 until p){
            val n:Int = sc.nextInt()
            if(m[n-1]==1){
                m[n-1] = 0
            }else{
                r++
            }
        }
        println(r)
    }
}