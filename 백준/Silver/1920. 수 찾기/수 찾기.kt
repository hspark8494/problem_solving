fun main(){
    readLine()
    val list = readLine()!!.split(" ").map { it.toInt() }.sorted()
    readLine()
    val data = readLine()!!.split(" ").map{it.toInt()}
    for(i in data){
        println(if(list.binarySearch(i) > -1) 1 else 0)
    }
}