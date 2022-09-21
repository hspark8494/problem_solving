fun main(){
    for(x in 1 .. readLine()!!.toInt()) {
        val s = readLine()!!
        println("${s[0]}${s.last()}")
    }
}