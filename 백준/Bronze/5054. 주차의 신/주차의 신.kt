import kotlin.math.abs

fun main() {
    repeat(readLine()!!.toInt()){
        readLine()
        val l = readLine()!!.split(" ").map { it.toInt() }.sorted()
        val dist = MutableList<Int>(0){0}

        for(i in 0.. l.size-2){
            dist.add(abs((l[i]-l[i+1])*2))
        }
        
        println(dist.sum())
    }
}
