fun main(){
    var recodes :Array<Recode> = Array<Recode>(8){
        Recode(readLine()!!.toInt(), it+1)
    }

    recodes.sortWith(kotlin.Comparator { o1, o2 -> -(o1.score - o2.score) })
    recodes = recodes.slice(0..4).toTypedArray();
    println(recodes.sumOf { it.score })
    recodes.sortedBy { it.index }.forEach { print("${it.index} ") }
}
data class Recode(val score:Int, val index:Int)