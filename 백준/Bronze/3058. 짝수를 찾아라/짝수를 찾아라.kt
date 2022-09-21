fun main(){
    for(x in 1 .. readLine()!!.toInt()){
        val list = readLine()!!.split(" ").map { t -> t.toInt()}.filter { t-> t%2==0 }
        println("${list.sum()} ${list.minOrNull()} ")
    }
}