import java.util.*

fun main() {
    val init = readLine()!!.toInt()
    val arr = readLine()!!.split(" ").map { it.toInt() }
    val result:Array<Int> = Array(init){0}
    val map:MutableMap<Int, MutableList<Int>> = TreeMap<Int, MutableList<Int>>()

    for(i in arr.indices){
        if(map.contains(arr[i])){
            map[arr[i]]?.add(i)
        }else{
            map[arr[i]] = MutableList<Int>(1) { i }
        }
    }

    for((index, key) in map.keys.withIndex()){
        for(r in map[key]!!){
            result[r] = index
        }
    }
    print(result.joinToString(separator = " "))
}
