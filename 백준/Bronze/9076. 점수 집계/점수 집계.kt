fun main(){
    for(x in 0 until readLine()!!.toInt()){
        val list:List<Int> = readLine()!!.split(" ").map { it.toInt() }.sorted()
        if(list[3]-list[1] >= 4){
            println("KIN")
        }else{
            println(list.slice(1 .. 3).sum())
        }
    }
}