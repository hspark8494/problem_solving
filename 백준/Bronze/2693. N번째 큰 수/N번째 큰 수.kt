fun main(){
    for(i in 1..readLine()!!.toInt()){
        println(readLine()!!.split(" ").map{it.toInt()}.sorted()[7])
    }
}