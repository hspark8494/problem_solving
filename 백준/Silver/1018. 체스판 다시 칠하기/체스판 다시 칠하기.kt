import kotlin.math.min

val bTempl:String = "BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"
val wTempl:String = "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"
fun main(){
    val l = readLine()!!.split(" ")
    val row = l[0].toInt()
    val col = l[1].toInt()
    val list:List<String> = List<String>(row){readLine()!!}
    var minVal = Int.MAX_VALUE
    for(i in 0..row-8){
        for(j in 0..col-8){
            minVal = min(minVal, check(StringBuilder().apply {
                for(k in 0..7){
                    append(list[i+k].substring(j,j+8))
                }
            }.toString()))
        }
    }

    print(minVal)
}

fun check(text:String):Int{
    var white = 0
    var black = 0
    for(i in text.indices){
        if(text[i] == bTempl[i]){
            black++;
        }
        if(text[i] == wTempl[i]){
            white++;
        }
    }
    return min(black, white)
}